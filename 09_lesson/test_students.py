from sqlalchemy import create_engine, inspect, text

db_connection_string = "postgresql://postgres:9013@localhost:5432/QA"
engine = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(engine)
    assert 'users' in inspector.get_table_names()


def test_insert_and_delete():
    # engine.begin() автоматически открывает транзакцию и делает commit в конце
    with engine.begin() as connection:
        # Вставляем данные
        sql_insert = text(
            "INSERT INTO users(\"user_email\") VALUES (:new_name)")
        connection.execute(sql_insert, {"new_name": "test_unique@mail.com"})

        # Проверяем наличие
        result = connection.execute(
            text("SELECT count(*) FROM users WHERE user_email = :email"),
            {"email": "test_unique@mail.com"}
        ).scalar()
        assert result == 1

        # Очищаем за собой (чтобы тест можно было запустить снова)
        connection.execute(
            text("DELETE FROM users WHERE user_email = :email"),
            {"email": "test_unique@mail.com"}
        )


def test_update():
    with engine.begin() as connection:
        # Подготовка данных
        email = "update_test@mail.com"
        connection.execute(
            text("INSERT INTO users(\"user_email\") VALUES (:email)"),
            {"email": email})

        # Обновление
        sql_update = text(
            "UPDATE users SET \"subject_id\" = :sub_id WHERE \"user_email\" = :email")
        connection.execute(sql_update, {"sub_id": 1000, "email": email})

        # Проверка
        updated_val = connection.execute(
            text("SELECT subject_id FROM users WHERE user_email = :email"),
            {"email": email}
        ).scalar()
        assert updated_val == 1000

        # Удаление
        connection.execute(text("DELETE FROM users WHERE user_email = :email"),
                           {"email": email})
