def draw_pifagoras_tree(branch_length, level, angle=45):
    if level == 0:
        return
    print(" " * level, "+" + "-" * branch_length)  # Візуалізація гілки дерева
    draw_pifagoras_tree(branch_length, level-1, angle)  # Виклик функції для лівої гілки
    print(" " * level, "+" + "-" * branch_length)  # Візуалізація гілки дерева
    draw_pifagoras_tree(branch_length, level-1, -angle)  # Виклик функції для правої гілки

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії: "))
    branch_length = 3

    # Виклик рекурсивної функції для малювання дерева Піфагора
    draw_pifagoras_tree(branch_length, level)

if __name__ == "__main__":
    main()
