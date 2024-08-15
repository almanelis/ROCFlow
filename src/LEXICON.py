translations = {
    "Русский": {
        "nav": "Навигация",
        "ROC_Analyse_btn": ":chart_with_upwards_trend: ROC Анализ",
        "User_Manual_btn": ":bulb: Руководство пользователя",
        "title": ":chart_with_upwards_trend: Интерактивный сервис ROC-анализа",
        "description": "Это приложение выполняет ROC-анализ ваших"
                       " данных бинарной классификации. "
                       "Пожалуйста, загрузите файл CSV или Excel, содержащий "
                       "истинные метки и прогнозируемые вероятности.",
        "choose_file": "Выберите CSV или Excel файл",
        "file_reading_error": "Ошибка при чтении файла",
        "data_preview": "Просмотр данных:",
        'input_label_1': "Выберите столбцы с истинными значениями",
        "input_error_1": "Ошибка: истинные значения должны быть двоичными."
                         " Найдено",
        "input_error_11": "уникальных значений",
        "input_label_2": "Выберите стобцы с предсказанной вероятностью",
        "input_error_2": "Ошибка: Предсказанная вероятность должна быть"
        " в диапазоне от 0 до 1.",
        "treshold_title": ":scales: Интерактивный выбор Порогового значения",
        "specificity": "1 - Специфичность",
        "sensitivity": "Чувствительность",
        "treshold_select": "Выберите Пороговое значение",
        "current_treshold": "Выбранное Порогое значение",
        "sensitivity_treshold": "Чувствительность при выбранном Пороговом"
                                " значении",
        "specificity_treshold": "Специфичность при текущем Пороговом значении",
        "cmatrix_title": "🔢 Матрица Ошибок",
        "additional_metrics": ":straight_ruler: Дополнительные Показатели",
        "cmatrix_visualization": ":skin-tone-2: Визуализация Матрицы Ошибок",
        "user_manual_title": "Руководство пользователя",
        "user_manual_text": """
                    Добро пожаловать в интерактивный сервис **ROCFlow**! Данное
                    руководство пользователя поможет вам в использовании
                    приложения.

                    ## Приступим к работе
                    1. Подготовьте свои данные в формате CSV или Excel. Файл
                    должен содержать как минимум два столбца:
                    - Первый столбец из истинных значений (двоичных: 0 или 1,
                    отрицательных или положительных)
                    - Второй столбец из предсказанных вероятностей (от 0 до 1)

                    2. Загрузите свой файл с помощью программы загрузки файлов
                    на главной странице.

                    3. Выберите столбцы с истинными значениями и
                    предсказанными вероятностями в выпадающих меню.

                    4. Ниже появятся результаты анализа.

                    ## Что в результате?

                    - **ROC кривая** - это график, который иллюстрирует
                    производительность классификационной модели при всех
                    возможных порогах классификации.
                    - **AUC (Area Under the Curve)** - это мера, которая
                    позволяет суммировать производительность модели одним
                    числом, измеряя площадь под кривой ROC. AUC колеблется
                    от 0 до 1, где более высокое значение AUC указывает на
                    более высокую производительность модели.
                    - **Интерактивный выбор Порогового значения**: используйте
                    ползунок, чтобы увидеть, как различные пороговые
                    значения классификации влияют на показатели
                    производительности модели.
                    - **Матрица Ошибок**: Показывает количество истинно
                    положительных, истинно отрицательных, ложноположительных
                    и ложноотрицательных результатов при выбранном пороговом
                    значении.
                    - **Дополнительные Показатели**: включают accuracy,
                    precision, recall, f1 score.

                    ## Советы и рекомендации
                    - Поэкспериментируйте с различными пороговыми значениями,
                    чтобы найти оптимальный баланс между чувствительностью и
                    специфичностью для вашего конкретного случая.
                    - Оптимальный порог обычно выбирается как точка на кривой
                    ROC, которая находится ближе всего к верхнему левому
                    углу, поскольку это максимизирует истинный процент
                    положительных результатов при минимизации
                    ложноположительных результатов.
                    - На практике оптимальный порог может также зависеть от
                    конкретных целей задачи и затрат, связанных с
                    ложноположительными и ложноотрицательными результатами.

                    Если у вас есть какие-либо вопросы или вы столкнетесь с
                    какими-либо проблемами, пожалуйста, свяжитесь сo мной.
                    [almanelis](https://github.com/almanelis/)
                """


    },
    "English": {
        "nav": "Navigation",
        "ROC_Analyse_btn": ":chart_with_upwards_trend: ROC Analysis",
        "User_Manual_btn": ":bulb: User Manual",
        "title": ":chart_with_upwards_trend: Interactive ROC Analysis Service",
        "description": "This app performs ROC analysis on your binary"
        " classification data. "
                       "Please upload a CSV or Excel file containing true"
                       " labels and predicted probabilities.",
        "choose_file": "Choose a CSV or Excel file",
        "file_reading_error": "Error reading the file",
        "data_preview": "Data Preview:",
        'input_label_1': "Select the column with true labels",
        "input_error_1": "Error: The true labels should be binary. Found",
        "input_error_11": "unique values",
        "input_label_2": "Select the column with predicted probabilities",
        "input_error_2": "Error: Predicted probabilities should be between 0"
        " and 1.",
        "specificity": "1 - Specificity",
        "sensitivity": "Sensitivity",
        "treshold_title": ":scales: Interactive Threshold Selector",
        "treshold_select": "Select a threshold",
        "current_treshold": "Current Threshold",
        "sensitivity_treshold": "Sensitivity at Current Threshold",
        "specificity_treshold": "Specificity at Current Threshold",
        "cmatrix_title": "🔢 Confusion Matrix",
        "additional_metrics": ":straight_ruler: Additional Metrics",
        "cmatrix_visualization": ":skin-tone-2: Confusion Matrix"
                                 " Visualization",
        "user_manual_title": "User Manual",
        "user_manual_text": """
                Welcome to the Interactive ROC Analysis Service! This user
                manual will guide you through using the application.

                ## Getting Started
                1. Prepare your data in a CSV or Excel file. The file should
                contain at least two columns:
                - One column for true labels (binary: 0 or 1, negative or
                positive)
                - One column for predicted probabilities (continuous values
                between 0 and 1)

                2. Upload your file using the file uploader on the main page.

                3. Select the appropriate columns for true labels and
                predicted probabilities.

                4. Click the "Perform ROC Analysis" button to generate results.

                ## Understanding the Results
                - **ROC Curve**: This graph shows the trade-off between the
                true positive rate (sensitivity) and false positive rate (1 -
                specificity) at various classification thresholds.

                - **AUC (Area Under the Curve)**: A measure of the model's
                overall performance. Higher AUC indicates better performance.

                - **Interactive Threshold Selector**: Use this slider to see
                how different classification thresholds affect the model's
                performance metrics.

                - **Confusion Matrix**: Shows the number of true positives,
                true negatives, false positives, and false negatives at the
                selected threshold.

                - **Additional Metrics**: Includes accuracy, precision, and F1
                score at the selected threshold.

                ## Tips
                - Experiment with different thresholds to find the optimal
                balance between sensitivity and specificity for your
                specific use case.
                - The optimal threshold often depends on the relative costs of
                false positives and false negatives in your application.

                If you have any questions or encounter any issues, please
                contact me.
                [almanelis](https://github.com/almanelis/)
                """,
    }
}
