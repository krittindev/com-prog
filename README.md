# com-prog

[Grader](https://2110101.nattee.net/python/main/list) | 
[MyCourseView](https://www.mycourseville.com/?q=courseville/course/32196) |
[Syllabus](https://mycourseville-default.s3.ap-southeast-1.amazonaws.com/useruploaded_course_files/2022_2/32196/materials/CourseSyllabus_2110101_2_2565-5207-16735978797587.pdf) |
[Python101](https://www.cp.eng.chula.ac.th/~somchai/python101/)

## Tricks

### Excel URL extraction

- Tools > Macro > Visual Basic Editor
- insert module
    -```vbscript
    Function URL(Hyperlink As Range)
    URL = Hyperlink.Hyperlinks(1).Address
    End Function```
- insert cell `=URL({URL_CELL})`

### Create Multi Folder

```bash
mkdir folder_1 folder_2
```

### Create Multi File

```bash
touch folder_1/file1.py folder_2/file2.py
```
