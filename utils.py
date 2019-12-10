from tabulate import tabulate
import io


def multiply_list(list):
    # Multiply elements one by one
    result = 1
    for x in list:
        result = result * x
    return result


HEADING_TEMPLATE = "### Размер выборки - {} ###\n### λ = {} ###\n"


def report_erlang(filename, headers, values, selection_size, _lambda):
    with io.open(filename, "w", encoding="utf-8") as file:
        file.write(HEADING_TEMPLATE.format(selection_size, _lambda))
        file.write(
            tabulate(
                values, headers
            )
        )


TEST_TEMPLATE = "{value:.3f} {sign} {delta:.3f} | test {result}"
RESULT_TEMPLATE = "\nNumber of tests: {}\nTests passed: {}\nTests failed: {}"
HEADING_TEMPLATE_STUDENT = "### Размер выборки - {} ###\n### m = {} ###\n### Количество тестов - {} ###\n"


def get_test_result(value, delta):
    return ['<', 'passed'] if value < delta else ['>=', 'failed']


def format_test_result(value, delta, k=None):
    template = TEST_TEMPLATE
    if k:
        template = 'k = {k} | ' + TEST_TEMPLATE
    sign, result = get_test_result(value, delta)
    return template.format(k=k, value=value, sign=sign, delta=delta, result=result)


def report_student(filename, headers, values, test_results, selection_size, m, mode="w+"):
    failed = 0
    passed = 0
    for test_result in test_results:
        if "failed" in test_result:
            failed = failed + 1
        else:
            passed = passed + 1

    with io.open(filename, mode, encoding="utf-8") as file:
        file.write(HEADING_TEMPLATE_STUDENT.format(selection_size, m, len(test_results)))
        file.write(
            tabulate(
                values, headers
            )
        )
        file.write("\n\nTests: \n")
        for test_result in test_results:
            file.write(test_result)
            file.write("\n")
        file.write(RESULT_TEMPLATE.format(len(test_results), passed, failed))
