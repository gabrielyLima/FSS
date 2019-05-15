from FSS import FSS
from ObjectiveFunction import *
from SearchSpaceInitializer import UniformSSInitializer

def main():
    objective_function = RastriginFunction(dim=30)
    search_space_initializer = UniformSSInitializer()
    num_exec = 30
    school_size = 30
    num_iterations = 9000
    step_individual_init = 0.1
    step_individual_final = 0.0001
    step_volitive_init = 0.01
    step_volitive_final = 0.001
    min_w = 1
    w_scale = num_iterations / 2.0
    cost_all = []

    for _ in range(num_exec):
        f = FSS(objective_function=objective_function, search_space_initializer=search_space_initializer,
                n_iter=num_iterations, school_size=school_size, step_individual_init=step_individual_init,
                step_individual_final=step_individual_final, step_volitive_init=step_volitive_init,
                step_volitive_final=step_volitive_final, min_w=min_w, w_scale=w_scale)
        f.optimize()
        cost_all.append(f.optimum_cost_tracking_iter)
    print(cost_all)

    avg_cost = []
    for i in range(8334): #fitness_assessment
        sum = 0
        for j in range(num_exec):
            sum += cost_all[j][i]
        media = sum/num_exec
        avg_cost.append(media)
    print(avg_cost)

    for y in range(len(avg_cost)):
        arquivo = open("FSS_RastriginFunction.txt", "a")
        arquivo.writelines(str(avg_cost[y]) + ", ")

if __name__ == "__main__":
    main()