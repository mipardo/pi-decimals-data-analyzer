from data_loader import load_omp_results_from_file
import matplotlib.pyplot as plt
import numpy as np
import styles


def generate_comparison_execution_times_plot(precision_used, execution_times):
    # Set the figure within the subplot
    fig, ax = plt.subplots(figsize=(9, 6))

    # Draw the execution times for each algorithm
    i = 0
    for algorithm in execution_times.keys():
        ax.plot(precision_used, execution_times[algorithm], color=styles.color_lines[i], marker=styles.marker_styles[i],
                linestyle='solid', linewidth=1.5, markersize=5, label=algorithm)
        i += 1

    # Set axis limits and steps
    plt.grid(axis='y')

    # Set tittles:
    plt.xlabel('Precisión', fontdict=styles.font_subtitle)
    plt.ylabel('Tiempo de ejecución (s)', fontdict=styles.font_subtitle)
    if styles.show_plots_title:
        plt.title("Comparación de los tiempos de ejecución de los algoritmos secuenciales", fontdict=styles.font_title)


    # Show legend
    plt.legend(loc='upper left')

    # plt.show()
    plt.savefig(f"{path_to_save}ex-seq-comparison.png")
    plt.close()


if __name__ == '__main__':
    # Set file and path to store the plots
    results_path = styles.omp_results_file
    path_to_save = 'plots/'

    data = load_omp_results_from_file(results_path)

    seq_exec_times = dict()  # seq_exec_times = { algorithm_tag : [seq_times] }
    for algorithm_key in data.keys():
        seq_times = list()
        for precision_key in data[algorithm_key].keys():
            seq_times.append(data[algorithm_key][precision_key][1])
        seq_exec_times[algorithm_key] = seq_times
        seq_exec_times[algorithm_key].reverse()

    precision_used = list(data[algorithm_key].keys())
    precision_used.reverse()

    generate_comparison_execution_times_plot(precision_used, seq_exec_times)