class LatticeIsing_2D():
    def __init__(self, N, J, h):
        """
        Attributes:
            N: 格子サイズ
            J: 相互作用
            h: 磁場
        """
        self.N = N
        self.J = J
        self.h = h

    def neighor_spin_sum(self, state, x, y):

        center_spin = state[y, x]
        right, left, up, down = x+1, x-1, y+1, y-1

        # 周期境界条件
        if right >= self.N:
            right_spin = state[y, 0]
        else:
            right_spin = state[y, right]

        if left < 0:
            left = self.N-1
            left_spin = state[y, left]
        else:
            left_spin = state[y, left]

        if down < 0:
            down = self.N-1
            down_spin = state[down, x]
        else:
            down_spin = state[down, x]

        if up >= self.N:
            up_spin = state[0, x]
        else:
            up_spin = state[up, x]

        neighor_spin_sum = self.J * center_spin * \
            (right_spin+left_spin+up_spin+down_spin)
        return neighor_spin_sum

    # エネルギーを計算
    def energy(self, state):
        energy = 0
        for x in range(self.N):
            for y in range(self.N):
                energy -= self.neighor_spin_sum(state, x, y)/2
        energy -= self.h*np.sum(state)
        return energy

    # 磁化を計算
    def magnetization(self, state):
        return np.mean(state)
