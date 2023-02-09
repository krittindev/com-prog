[documentation](https://mermaid.js.org/syntax/flowchart.html)
```mermaid
graph TB

    START([Start])
    END([End])
    INPUT[/input x1, y1, r1, x2, y2, r2/]
    CON1{"((x1-x2)**2 + \n(y1-y2)**2)**0.5 \n== r1 + r2"}
    CON2{"((x1-x2)**2 + \n(y1-y2)**2)**0.5 \n< r1 + r2"}

    OUTPUT1[/print 1/]
    OUTPUT2[/print 2/]
    OUTPUT3[/print 3/]
    START --> INPUT
    INPUT --> CON1
    CON1 --True--> OUTPUT1
    CON1 --False--> CON2
    CON2 --True--> OUTPUT2
    CON2 --False--> OUTPUT3
    OUTPUT1 & OUTPUT2 & OUTPUT3 --> END
```