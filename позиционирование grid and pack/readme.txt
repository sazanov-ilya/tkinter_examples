В данном примере использовались два менеджера геометрии. Каждая рамка привязана к определенному окну через менеджер геометрии grid()

Каждый ярлык с текстом привязан к определенной рамки через менеджер .pack()

Важно понимать, что метод .grid() вызывается для каждого объекта рамки, но менеджер геометрии применяется к окну. Аналогично, расположение каждой рамки контролируется менеджером геометрии .pack().

Есть два вида отступов — внешние и внутренние. Внешнее отступы добавляют пространство вокруг ячейки сетки. Управление осуществляется через два ключевые аргумента метода


- padx - добавляет отступ в пикселях в горизонтальном направлении
- pady - добавляет отступы в пикселях в вертикальном направлении


Можно настроить так, чтобы строки и столбы сетки будут реагировать на изменение размера окна с помощью метода .columnconfigure() и .rowconfigure() для объекта окна приложения. Помните, что сетка привязана к окну, даже если вы вызываете метод .grid() для каждой рамки. Метод .columnconfigure() и .rowconfigure() принимают три важных аргумента:

Индекс столбца или строки сетки, которого нужно настроить (или список индексов для настройки нескольких строк или столбцов одновременно);
Ключевой аргумент под названием weight, который определяет, как столбец или строка должны реагировать на изменение размера окна относительно других столбцов и строк;
Ключевой аргумент под названием minsize, который устанавливает минимальный размер высоты строки или ширины столбца в пикселях.
Аргумент weight по умолчанию равен 0 . Это означает, что столбец или строка не расширяются при изменении размера окна. Если каждому столбцу и строке присвоен weight=1, то все они будут меняться одинаково. Если вес (weight) одного столбца 1, а у другого 2, то второй столбец расширяется вдвое быстрее первого.