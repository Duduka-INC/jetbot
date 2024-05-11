# ТЗ для финального дз по Голубову.

## Предисловие.

Если всем похер на то, что я написал ниже, то можем обойтись без этого, но так процесс будет более понятным и структурированным,
а ещё так работают в большинстве IT/инженерных коллективов, поэтому и предлагаю такой вариант. 

## Немножко про процесс разработки.

Прошу всех, кто причастен к разработке и будет писать код, придерживаться правил описанных в файле [CODESTYLE.md](./CODESTYLE.md).
Теперь о работе в гитхабе:

1. Когда вы приступаете к своей части работы, вы создаете новую ветку от нашей krbo_02 и коммитите свои изменения туда.
Ветку называйте по области задачи, типа: InfProcessing, либо по фамилии программиста, который это пишет.
2. После окончания работы, создается pull request в ветку krbo_02, который будет проверять и одобрять кто-то, кто шарит за всю архитектуру.
Проект не маленький, и если об этом не печься. то мы потом умрем писать адаптеры на все подряд и ничего не поймем.


## Общая постановка задачи.

По итогу мы (я) пришли к следующим особенностям от которых будет зависеть архитектура проекта:

- Так как внутри малыша не так много ~~мозгов~~ вычислительных мощностей, вся магия будет происходить на компе.


- Роботу будут отсылаться только команды, связанные с его движением, то есть скорость и флаг start/stop.


- Поток фоток приходит и обрабатывается на компутере.


- Необходимо сопоставить изображения с камер и объединить общие зоны, а также пошаманить с рыбьим глазом.

## Общее описание и структура проекта.

Перейдем к описанию работы программы.
В программе существуют два основных модуля, отвечающие за разные вещи, которые будут выполняться как два отдельных потока:

1. Первый отвечает за обработку изображения, получения координат робота и точек.
2. Второй отвечает за просчет траектории, учет ошибки и перевод ее в конкретные команды для движения робота.

### Модуль обработки информации.

- Необходимо написать main класс, в котором будут вызываться все остальные классы для обработки, склейки и т.д. 
Именно он будет постоянно принимать поток фоток.


-  Существует отдельный класс калибровщик, который принимает на вход изображение с шахматной доской, 
а возвращает матрицу нормирования и дисперсии. 
Он вызывается перед выставлением точек на поле и калибрует камеру, убирая fishEye и нормализуя изображение.


- Ввиду того, что области видимостей камер пересекаются, необходимо создать логику переключения между камерами, либо класс, 
который будет строить полную карту со всех камер, убирая перекрестные зоны. 


- Также должен быть отдельный класс детектор точек и робота, определяет их координаты в уже нормированной системе.

Схема работы одной итерации цикла обработки изображения такая (уже после калибровки камер и нахождения нормирующих матриц):

1. Чтение изображения из потока;
2. Нормирование;
3. Нахождение робота и точек (если нужно);
4. Запись координат в общий для 2-х модулей поток вывода, чтобы это мог считать второй модуль управления; 

### Модуль управления.

- Как и в предыдущем модуле нужен бесконечный поток получения данных и общий агрегатор всей логики, описанной ниже.


- Необходимо создать класс для просчета траектории и корректировки ошибки, который будет принимать на вход координаты 
робота и точек, сравнивая их с предыдущими, возвращая скорректированные параметры.


- Отдельный класс будет переводить созданную ранее траекторию в команды для робота (мощность на левом и правом двигателе).


- Также нужно разработать логику отправки команд роботу по ssh. Схема такая: перезапись txt файла с тремя параметрами 
(флаг, скорость левого и правого колес) внутри файловой системы робота.

Схема работы одной итерации цикла расчета траектории такая (уже после калибровки камер и нахождения нормирующих матриц):

1. Чтение координат из потока; 
2. Определение ошибки и расхождения с предыдущей траекторией;
3. Корректировка траектории;
4. Перевод траектории в команды для робота;
5. Передача команд роботу;


### Общие для 2-х модулей вещи.

Нужно сделать синхронизацию потоков как-то и понять, что это вообще, пока что это файл .csv для первого модуля и .txt для второго.

Ещё я пока не додумал пару моментов, главный из них:
Как вообще реализовать правильно второй модуль? Но я уверен, 
что Федя поможет нам всем и проведет КРБО-шный народ через пустыню к обетованному зачету. 

Пока вроде все...