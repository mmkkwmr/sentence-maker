import subprocess


def test_three_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校 昼寝\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "猫" in result.stdout
    assert "学校" in result.stdout
    assert "昼寝" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_four_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校 昼寝 お菓子\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "猫" in result.stdout
    assert "学校" in result.stdout
    assert "昼寝" in result.stdout
    assert "お菓子" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_five_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校 昼寝 お菓子 友達\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "猫" in result.stdout
    assert "学校" in result.stdout
    assert "昼寝" in result.stdout
    assert "お菓子" in result.stdout
    assert "友達" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_two_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校\n",
        text=True,
        capture_output=True
    )

    assert result.returncode != 0


def test_six_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校 昼寝 お菓子 友達 公園\n",
        text=True,
        capture_output=True
    )

    assert result.returncode != 0
def test_invalid_word_count():
    result = subprocess.run(
        ["./sentencemaker"],
        input="猫 学校\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == "単語は3〜5個で入力してください。\n"
