from threading import Timer


def debounce(f, n):
    t = None

    def result():
        nonlocal t
        if t:
            t.cancel()
        t = Timer(n // 1000, f)
        t.start()
    return result


def test_print():
    print("Hello, world!")


debounced = debounce(test_print, 2000)
debounced()
