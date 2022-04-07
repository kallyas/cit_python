"""
1. .Convert the halving & block frequency in a line graph. 
xaxis represent the bitcoin rewards and yaxis
represent the number of bitcoin supply.

"""

def halving_block_frequency(reward_list):
    """
    This function will take a list of rewards and return a list of
    halving and block frequency.
    """
    halving_frequency = []
    block_frequency = []
    for i in range(len(reward_list)):
        if i == 0:
            halving_frequency.append(0)
            block_frequency.append(0)
        else:
            halving_frequency.append(reward_list[i]/reward_list[i-1])
            block_frequency.append(i)
    return halving_frequency, block_frequency


def create_reward_list():
    year = 2009
    sRewards = 50 * 10**8
    reward_list = []
    btcMined = 0
    while year <= 2018:
        if year == 2009:
            reward_list.append(sRewards)
        else:
            sRewards = sRewards / 2
            reward_list.append(sRewards)
        year += 4
    return reward_list


def main():
    import matplotlib.pyplot as plt
    reward_list = create_reward_list()
    halving_frequency, block_frequency = halving_block_frequency(reward_list)
    plt.plot(block_frequency, halving_frequency)
    plt.xlabel("Block Frequency")
    plt.ylabel("Halving Frequency")
    plt.title("Halving Frequency vs Block Frequency")
    plt.show()


if __name__ == "__main__":
    main()