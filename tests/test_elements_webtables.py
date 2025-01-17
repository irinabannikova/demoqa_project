from pages.element_page_webtables import ElementsPageWebTables
import pytest

def test_add_valid_record(page):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.add_new_record(
        "Irina1",
        "Bannikova",
        "test1@mail.com",
        "51",
        "30000",
        "test"
    )
    web_table.review_add_valid_new_record()



@pytest.mark.parametrize("first_name, last_name, email, age, salary, departament", [
    ("", "Bannikova", "test1@mail.com", "1", "30000", "test"),
    ("Irina1", "", "test1@mail.com", "10", "30000", "test"),
    ("Irina1", "Bannikova", "", "21", "30000", "test"),
    ("Irina1", "Bannikova", "test1@mail.com", "", "30000", "test"),
    ("Irina1", "Bannikova", "test1@mail.com", "41", "", "test"),
    ("Irina1", "Bannikova", "test1@mail.com", "51", "30000", ""),
    ("Irina1", "Bannikova", "test1mailcom", "51", "30000", "test")
])
def test_add_invalid_record(page, first_name, last_name, email, age, salary, departament):
    web_table = ElementsPageWebTables(page)

    web_table.go_to_task_web_tabel()
    web_table.add_new_record(first_name, last_name, email, age, salary, departament)
    web_table.review_add_invalid_record()

def test_add_record_with_max_length(page):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.add_new_record(
        "irinairinairinairinairinaaa",
        "bannikovabannikovabannikottttt",
        "test1@mail.com",
        "513454",
        "300000000023455",
        "testtesttesttesttesttesttyyyyy"
    )
    web_table.review_add_max_value()

def test_edit_old_record(page):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.edit_old_record("Irina1",
                              "Bannikova",
                              "test1@mail.com",
                              "51",
                              "30000",
                              "test")
    web_table.review_edit_old_record()

def test_delete_record(page):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.delete_record()


@pytest.mark.parametrize("value", [
    "Kierra",
    " ",
    "Gentry",
    "29",
    "kierra@example.com",
    "2000",
    "Legal"
])
def test_type_to_search(page, value):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.input_to_search(value)
    web_table.review_result_to_search()

@pytest.mark.parametrize("rows", [
    "5",
    "10",
    "20",
    "25",
    "50",
    "100"
])
def test_edit_view_row(page,rows):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.select_num_rows(rows)

def test_add_many_records(page):
    web_table = ElementsPageWebTables(page)
    web_table.go_to_task_web_tabel()
    web_table.add_many_record(
        "Irina1",
        "Bannikova",
        "test1@mail.com",
        "51",
        "30000",
        "test"
    )
    web_table.review_next_button()


