# laserchat
0) Ставим все зависимости

pip install numpy

pip install pymorphy2

pip install -U scikit-learn

pip install pandas

pip install laserembeddings

python -m laserembeddings download-models

1) Подготавливаем вопросы и ответы в формате как в файле boltun.txt
2) Запускаем convertboltuntxttocsv.py который сконвертирует boltun.txt в boltun.csv
3) Запускаем laserchat - и пишем какую-нибудь фразу или вопрос боту

(имеющийся набор фраз взят из моего Android-ассистента Лилии, и содержит кроме всего прочего некоторое количество специфичных для данной программы фраз)
