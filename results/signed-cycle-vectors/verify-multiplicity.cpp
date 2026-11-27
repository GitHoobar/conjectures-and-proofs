// Direct cycle counts on small signed complete graphs, independent of the forest inventory.
#include <cstdint>
#include <iostream>
#include <stdexcept>
#include <utility>
#include <vector>

using Matrix = std::vector<std::vector<int>>;
using Counts = std::vector<std::int64_t>;

Matrix all_positive(int n) {
    return Matrix(n, std::vector<int>(n, 1));
}

void negate_edge(Matrix& graph, int x, int y) {
    graph[x][y] = graph[y][x] = -1;
}

Matrix two_blocks(int bits) {
    Matrix graph = all_positive(19);
    // 0 is the marker, 1 and 2 are the anchors, and the private blocks begin at 3 and 11.
    negate_edge(graph, 0, 1);
    negate_edge(graph, 1, 2);
    const std::vector<std::pair<int, int>> common{
        {0,4},{0,5},{0,6},{1,5},{1,7},{2,6},{2,7},{4,5},{5,7},{6,7}
    };
    for (int block = 0; block < 2; ++block) {
        int offset = 3 + 8 * block;
        for (int i = 0; i < 8; ++i) negate_edge(graph, 1 + block, offset + i);
        for (auto [i,j] : common) negate_edge(graph, offset+i, offset+j);
        if ((bits >> block) & 1) {
            negate_edge(graph, offset+1, offset+6);
            negate_edge(graph, offset+3, offset+7);
        } else {
            negate_edge(graph, offset+3, offset+6);
            negate_edge(graph, offset+4, offset+7);
        }
    }
    return graph;
}

Counts signed_cycle_sums(const Matrix& graph) {
    const int n = static_cast<int>(graph.size());
    // At these test orders all signed sums fit in a signed 64-bit integer.
    if (n > 19) throw std::invalid_argument("direct checker supports at most 19 vertices");
    Counts sums(n+1);
    for (int first = 0; first < n-2; ++first) {
        int width = n-first-1;
        unsigned limit = 1u << width;
        Counts paths(static_cast<std::size_t>(limit)*width);
        std::vector<int> size(limit);
        for (unsigned mask = 1; mask < limit; ++mask) {
            size[mask] = 1 + size[mask & (mask-1)];
            for (int last = 0; last < width; ++last) {
                unsigned bit = 1u << last;
                if (!(mask & bit)) continue;
                unsigned previous = mask ^ bit;
                int end = first+1+last;
                std::int64_t total = 0;
                if (!previous) {
                    total = graph[first][end];
                } else {
                    for (int j = 0; j < width; ++j) {
                        if (previous & (1u << j))
                            total += paths[previous*width+j] * graph[first+1+j][end];
                    }
                    sums[size[mask]+1] += total * graph[end][first];
                }
                paths[mask*width+last] = total;
            }
        }
    }
    for (auto& total : sums) {
        if (total % 2) throw std::logic_error("orientation parity");
        total /= 2;
    }
    return sums;
}

int main() {
    // Calibrate sign, orientation, and length on K5 containing one negative edge.
    Matrix known = all_positive(5);
    negate_edge(known, 0, 1);
    if (signed_cycle_sums(known) != Counts{0,0,0,4,3,0})
        throw std::logic_error("K5 single-edge control failed");

    auto positive = signed_cycle_sums(all_positive(19));
    auto baseline = signed_cycle_sums(two_blocks(0));
    for (int bits = 1; bits < 4; ++bits) {
        if (signed_cycle_sums(two_blocks(bits)) != baseline)
            throw std::logic_error("cycle sums differ across choices");
    }
    std::cout << "All four 19-vertex graphs agree. Counts by cycle length:\n";
    for (int k = 3; k <= 19; ++k)
        std::cout << k << " " << (positive[k]-baseline[k])/2 << "\n";
}
