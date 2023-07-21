rm tables/*.tex
rm plots/*.png
mkdir tables plots

python3 latex_table_generator_hyb_algorithms.py
python3 latex_table_generator_hyb_comparison.py
python3 latex_table_generator_mpi_algorithms.py
python3 latex_table_generator_mpi_comparison.py
python3 latex_table_generator_omp_algorithms.py
python3 latex_table_generator_omp_comparison.py
python3 latex_table_generator_seq_comparison.py

python3 plot_generator_iterations_time.py

python3 plot_generator_hyb_algorithms.py
python3 plot_generator_hyb_comparison.py
python3 plot_generator_mpi_algorithms.py
python3 plot_generator_mpi_comparison.py
python3 plot_generator_omp_algorithms.py
python3 plot_generator_omp_comparison.py
python3 plot_generator_seq_comparison.py
