import scala.io.StdIn.readLine

object Main {

  def main(args: Array[String]): Unit = {
    //Task_a(args)
    //Task_b(args)
    //Task_c(args)
    //Task_d(args)
    //Task_e(args)
    //Task_f(args)
    //Task_g(args)
    //Task_h(args)
    // Что бы заработал n-ый таск нужно его раскомментировать здесь.
  }

  def Task_a(args: Array[String]): Unit = {

    println("Hello world!")
    // Выводим в консоль с переносом строки (ln)
    println("Hello world!".reverse)
    // Переворачиваем строку. Строка в данном случае объект
    println("Hello world!".toLowerCase)
    // Переносим строку в нижний регистр
    println("Hello world!".replace("!", ""))
    // Меняем ! на отсутствие символа
    print("Hello world!".replace("!", "").concat(" and goodbye python!"))
    // Убираем ! и присоединяем новую строку к старой
  }

  def Task_b(args: Array[String]): Unit = {
    val year_value = readLine().toInt
    // Получаем значение, сразу преобразуем его в int
    val upper_ = (100 - readLine().toDouble) / 100
    // Получаем значение, превращаем его в double.
    // Это значение в процентах -> сразу преобразуем его в нужный для вычисления множитель
    val eating_ = readLine()
    // Получаем число. Оно хранится пока что в строке
    val result_ = (year_value * 87 / 100 * upper_ - eating_.toInt) / 12
    // Вычисляем по формуле: годова зарплата * множитель без налога * процент без премии - компенсация за еду.
    // Всё делим на 12, так как все значения указаны в годовом объеме.
    print("Ежемесячный оклад сотрудника: " + result_)
  }

  def Task_c(strings: Array[String]): Unit ={
    val workers_ok = Array(100, 150, 200, 80, 120, 75)

    val year_value = readLine().toInt
    val upper_ = (100 - readLine().toDouble) / 100
    val eating_ = readLine()
    val result_ = (year_value * 87 / 100 * upper_ - eating_.toInt) / 12

    for (i <- workers_ok){
      // Достаем сотрудников в переменную i из массива workers_ok
      //println("Worker with payment " + i + " is taking " + (if (result_ < i)  "more" else "lesser") + " then middle!" )
      println("Worker with payment " + i + " is taking " + (i / result_ * 100).round + "% off middle payment!" )
      // Выводим зарплату сотрудника и сколько процентов от средней (введенной) зарплаты составляет зарплата сотрудника

    }
  }

  def Task_d(strings: Array[String]): Unit ={
    var workers_ok = Array(100, 150, 200, 80, 120, 75)
    // Задаем массив
    while (true) {
      // Пока истина (ВСЕГДА ХАХА) выполняем действия
      print("Want to know max and min of current payments? y/n ")

      var want_ = readLine()
      // Проверяем что хочет сделать пользователь: вывести максимум и минимум или изменить зарплату какого то работника
      if (want_ == "y" || want_ == "Y") {
        println("Max of current payments is: " + workers_ok.max)
        println("Min of current payments is: " + workers_ok.min)
        // Выводим максимум и минимум если пользователь отвечает y
      } else {
        // Иначе меняем зарплату
        println("Ok, dear! Lets change they's payment.")
        println("Here your workers:")
        for (worker <- workers_ok.indices) print((worker + 1) + ": " + workers_ok(worker))
        // Выводим номер пользователя и его зарплату
        println("")
        // Перенос строки
        print("Chose worker: ")
        var i = readLine().toInt
        // Даем выбрать работника
        print("Write the multiplier of his payment (%) : ")
        val multiply_ = readLine().toInt
        // Спрашиваем на сколько нужно умножить его зарплату
        workers_ok(i - 1) = workers_ok(i - 1) * multiply_.abs / 100
        // Умножаем зарплату на модуль процента  потом делим на 100
        print("Want to exit this code? y/n ")
        var exit_? = readLine()
        // Спрашиваем, хочет ли пользователь выйти из программы (не виляет ни на что)
        if (exit_? == "y"|| exit_? == "Y") println("AHAHAHAHAHA HERE IS NO EXIT AHAHAHAHAHA")
      }
    }
  }

  def Task_e(args: Array[String]): Unit = {
    var workers_ok = Array(100, 150, 200, 80, 120, 75)
    workers_ok = 90 +: workers_ok :+ 350
    // Левый (добавление слева) и правый (добавление справа) инкримент в массив
    for (worker <- workers_ok.sortBy(value => (value))) print(worker + " ")
    // Вывод зарплат. Здесь массив предварительно сортируем и именно из сортированного массива вытаскиеваем поэлементно.
    // Переменная workers_ok не изменияется. В ней лежит всё тот же не сортированный массив

  }

  def Task_f(args: Array[String]): Unit = {
    var workers_ok = Array(100, 150, 200, 80, 120, 75)
    workers_ok = (90 +: workers_ok :+ 350).sortBy(value => (value))
    // Получаем уже сортированный массив с 2-мя новыми элементами
    print("Enter a new worker's payment: ")
    var attach_ed = readLine().toInt
    // Получаем зарплату нового работника
    var result_ = new Array[Int](0)
    // Задаем пустой массив в который будем с будущем сгружать данные
    var temp = true
    // Условие ввода в массив. Значение изменилось - значит новую зарплату вставили
    for (worker <- workers_ok){
      // Проверяем, данная зарптата больше введенной или нет
      if (worker > attach_ed && temp) {
        result_ = result_ :+ attach_ed
        // Если больше - вставляем нашу новую зарплату в новый массив.
        temp = false
        // Говорим, что больше вводить не нужно
      }
      result_ = result_ :+ worker
      // Добавляем зарплату текущего пользователя в новый массив
    }

    for (worker <- result_) print(worker + " ")
    // Выводим зарплаты пользователей из нового массива
  }


  def Task_g(args: Array[String]): Unit = {

    var workers_ok = Array(100, 150, 200, 80, 120, 75)
    var temp = true
    // Усливие прекращения ввода вилки. Пока True - вилка либо не введена либо левый элемент больше правого
    var one_of_two = " - ".split("-")
    // Задаем переменную в которой будет храниться вилка
    while (temp){
      print("Enter payment vilky for middle worker (- as separator): ")
      one_of_two = readLine().split("-")
      // Получаем вилку в переменную
      if (one_of_two(0).toInt < one_of_two(1).toInt) temp = false else println("Try again, be a bit better...")
      // Проверяем, что левая граница меньше правой.
      // Если да - проодолжаем выполнение программы.
      // Иначе - просим ввести снова
    }

    for (worker <- workers_ok.indices) {
      if (workers_ok(worker) >= one_of_two(0).toInt && workers_ok(worker) <= one_of_two(1).toInt) println("Worker with id=" + (worker + 1) + " is Middle!")
    // Выводим пользвоателей, которое попадают в нашу вилку
  }

}

  def Task_h(args: Array[String]): Unit = {

    var workers_ok = Array(100, 150, 200, 80, 120, 75)
    println("Workers payment before krizis:")
    for (worker <- workers_ok) {
      print(worker + " ")
    }
    // Выводим наш старый список
    workers_ok = workers_ok.map(x => x * 93 / 100)
    // Через map обращаемся к каждому элементу массива и применяем к нему функцию
    println()
    println("Workers payment after krizis:")
    for (worker <- workers_ok) {
      print(worker + " ")
    }
    // Выводим измененный массив
  }
}
