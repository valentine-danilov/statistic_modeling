from tabulate import tabulate
import io

HEADING_TEMPLATE = "### Размер выборки - {} ###\n### λ = {} ###\n"


def report_erlang(filename, headers, values, selection_size, _lambda):
    with io.open(filename, "w", encoding="utf-8") as file:
        file.write(HEADING_TEMPLATE.format(selection_size, _lambda))
        file.write(
            tabulate(
                values, headers
            )
        )


def get_test_result(value, delta):
    return ['<', 'passed 👌'] if value < delta else ['>=', 'failed 😭']


TEST_TEMPLATE = '{value:.3f} {sign} {delta:.3f} | test {result}'


def format_test_result(value, delta, k=None):
    template = TEST_TEMPLATE
    if k:
        template = 'k = {k} | ' + TEST_TEMPLATE
    sign, result = get_test_result(value, delta)
    return template.format(k=k, value=value, sign=sign, delta=delta, result=result)
