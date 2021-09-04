"""
        target = len(arr) / 2

        if target == 1:
            return arr[0]

        x = Counter(arr)

        vals = list(x.values())

        print(vals)
        if all((x == 1) for x in vals):
            return int(target)

        if len(x.values()) == 1 or len(x.values()) == 2:
            return 1

        else:
            possible_combinations = combinations([i for i, v in x.items()], 2)

            accepted = []
            for pos_list in possible_combinations:
                res = list(filter(lambda i: i not in pos_list, arr))

                ic(res)
                if len(res) <= target:
                    print(len(res))

                    accepted.append(set(res))

            print(accepted)
            # return len(min(accepted))


"""
