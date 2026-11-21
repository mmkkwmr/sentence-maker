import subprocess


def test_three_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="私 洞窟 探検\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "私" in result.stdout
    assert "洞窟" in result.stdout
    assert "探検" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_four_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="女の子 公園 散歩 花\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "女の子" in result.stdout
    assert "公園" in result.stdout
    assert "散歩" in result.stdout
    assert "花" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_five_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="私 森 冒険 宝物 友達\n",
        text=True,
        capture_output=True
    )

    assert result.returncode == 0
    assert "私" in result.stdout
    assert "森" in result.stdout
    assert "冒険" in result.stdout
    assert "宝物" in result.stdout
    assert "友達" in result.stdout
    assert result.stdout.strip().endswith("。")


def test_two_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="私 洞窟\n",
        text=True,
        capture_output=True
    )

    assert result.returncode != 0


def test_six_words():
    result = subprocess.run(
        ["./sentencemaker"],
        input="私 森 冒険 宝物 友達 公園\n",
        text=True,
        capture_output=True
    )

    assert result.returncode != 0
