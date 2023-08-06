# Labos

Este paquete está dedicado principalmente a facilitar el uso de herramientas y paquetes utilizados en la adquisición y procesamiento de datos en el marco de los laboratorios de la carrera en [*Ciencias Físicas de la UBA*](https://www.df.uba.ar/es/).

Los paquetes hasta ahora implementados son de adquisición y análisis de datos.

<!-- headings -->
## Análisis de datos

### Propagación
Este paquete está dedicado a propagar errores utilizando una aproximación lineal sobre la formula de covarianza. El paquete está basado en las librerías numpy e sympy.
```python
from labos.propagacion import Propagacion_errores
import numpy as np

# Formula a propagar
expr = 'A*cos(f*t) + C'    

# Las variables dependientes y sus valores
variables = [
    ('f', 100), # Hz
    ('A', 2), # Volts
    ('t', 1), # s
    ('C', .5), # Volts
    ]

# Los errores de las variables
errores = np.array(
    [.0005,
    .0001, 
    0, 
    .0001]
    ).reshape(-1,1)

# Instancia de la clase
propaga = Propagacion_errores(
    formula = expr,
    variables = variables,
    errores = errores)
propaga.fit()
>>(2.224637744575368, 0.0005232992460070357)
```
### Ajuste
Este paquete está dedicado a realizar ajustes sobre datos. El paquete está basado en las librerías numpy e sympy.

#### Heading 3
##### Heading 4
###### Heading 5

<!-- line breaks -->
<!-- ENTER -->

<!-- Italics -->
This is an *italic* text

This is an _italic_ text

<!-- Strongs -->
This is an **strong** text

This is an __strong__ text

<!-- StrikeTrough -->
This is an ~~striketrogh~~ text



<!-- UL -->
* item 1
* item 2
* item 3
    * item 3.1
    * item 3.2    
* item 4

<!-- OL -->
1. item 1
1. item 2
1. item 3
1. item 4

<!-- Links -->
[Faztweb.com](https://www.faztweb.com)

[Faztweb.com](https://www.faztweb.com "Custom title")
<!-- Blockquote -->
> this is a quote

<!-- Horizontal Rule -->
___
---

<!-- Inline code -->
`console.log('hello world')`

`<h1>Hello world</h1>`

<!-- IMAGES -->
<!-- ![Vscode Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/1200px-Visual_Studio_Code_1.35_icon.svg.png) -->

<!-- ![Vscode logo](./vscode.png "vscode") -->

<!-- GITHUB MD -->

```
first line of code
second line of code
```

```python
print("hello world")
```

```javascript
console.log('hello world')

const test = (str) => str + 'test';
```

```html
<h1>Hello World</h1>
```

<!-- TABLES -->
| Product       | Price         |quantity   |
| ------------- |:-------------:| :--------:|
| Laptop        | 3.33          | 2         |
| Mouse         | 10.33         | 1         |

* [x] task1
* [] task2
* [] task3
* [x] task4

<!-- Mentiosn -->
@faztweb :+1: :smile:
