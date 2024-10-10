import timeit
from functions import camel_case, snake_case, pascal_case, kebab_case, upper_case, lower_case, alternate_case, title_case, reverse_text, remove_spaces

# Define o texto de exemplo para o teste
test_text = "exemplo de texto para testar performance"

# Medir a performance de cada função
execution_time_camel = timeit.timeit(f"camel_case('{test_text}')", setup="from functions import camel_case", number=250000)
execution_time_snake = timeit.timeit(f"snake_case('{test_text}')", setup="from functions import snake_case", number=250000)
execution_time_pascal = timeit.timeit(f"pascal_case('{test_text}')", setup="from functions import pascal_case", number=250000)
execution_time_kebab = timeit.timeit(f"kebab_case('{test_text}')", setup="from functions import kebab_case", number=250000)
execution_time_upper = timeit.timeit(f"upper_case('{test_text}')", setup="from functions import upper_case", number=250000)
execution_time_lower = timeit.timeit(f"lower_case('{test_text}')", setup="from functions import lower_case", number=250000)
execution_time_alternate = timeit.timeit(f"alternate_case('{test_text}')", setup="from functions import alternate_case", number=250000)
execution_time_title = timeit.timeit(f"title_case('{test_text}')", setup="from functions import title_case", number=250000)
execution_time_reverse = timeit.timeit(f"reverse_text('{test_text}')", setup="from functions import reverse_text", number=250000)
execution_time_remove_spaces = timeit.timeit(f"remove_spaces('{test_text}')", setup="from functions import remove_spaces", number=250000)

# dicionário para armazenar os tempos
execution_times = {
    "camel_case": execution_time_camel,
    "snake_case": execution_time_snake,
    "pascal_case": execution_time_pascal,
    "kebab_case": execution_time_kebab,
    "upper_case": execution_time_upper,
    "lower_case": execution_time_lower,
    "alternate_case": execution_time_alternate,
    "title_case": execution_time_title,
    "reverse_text": execution_time_reverse,
    "remove_spaces": execution_time_remove_spaces
}

# Ordenar os tempos do mais lento para o mais rápido
sorted_times = sorted(execution_times.items(), key=lambda x: x[1], reverse=True)

# Imprimir os resultados
print("\nTempos de execução (250k iterações):")
for func_name, exec_time in sorted_times:
    print(f"{func_name}: {exec_time:.4f} segundos")
