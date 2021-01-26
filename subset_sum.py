s = [163, 475, 160, 674, 85, 916, 461, 307, 349, 86, 198, 466, 709, 973, 981, 374, 766, 473, 342, 191, 393, 300, 11]

num = 3652
z = 0
sol = []


def backtrack(space):
    global sol, z

    for i in range(len(space)):
        next_num = space[i]
        if sum(sol) + next_num <= num:

            sol.append(next_num)
            curr_sum = sum(sol)
            new_space = space[i+1:]

            if curr_sum == num:
                z += 1
                print(sol)
            else:
                backtrack(new_space)

            sol.remove(next_num)


backtrack(s)
print(z)
