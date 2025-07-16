import pytest
from project import Questions, store, result

def test_questions_class():
    q = Questions("What is Python?", ["(a) Snake", "(b) Language"], "b")
    assert q.prompt == "What is Python?"
    assert q.answer == ["(a) Snake", "(b) Language"]
    assert q.correct == "b"

def test_store_creates_questions(monkeypatch):
    test_data = [
        ("Q1", ["(a) A", "(b) B"], "a"),
        ("Q2", ["(a) C", "(b) D"], "b"),
    ]

    captured = []

    def fake_run(questions, timeout=10):
        captured.append(questions)

    import project
    monkeypatch.setattr(project, "run", fake_run)

    store(test_data)
    assert len(captured[0]) == 2
    assert isinstance(captured[0][0], Questions)

def test_result_output(capsys):
    result(3, 5)
    captured = capsys.readouterr()
    assert "You got 3/5 questions correct!" in captured.out
    assert "You have scored 60%" in captured.out

