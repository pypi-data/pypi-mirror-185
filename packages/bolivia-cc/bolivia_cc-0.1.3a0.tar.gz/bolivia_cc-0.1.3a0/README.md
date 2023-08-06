# Bolivia Codigo de Control

El Código de control Es un dato alfanumérico generado e impreso por un sistema de facturación computarizado SFV al momento de emitir una factura y sirve sirve para determinar la validez o no de una factura.

Ejemplo: CB-5E-CF-8B-05

Está constituido por pares de datos alfanuméricos separados por guiones (-) y expresados en formato hexadecimal (A, B, C, D, E y F), no contene la letra “O” solamente el número cero (0). Se genera en base a información de dosificación de la transacción comercial y la llave asignada a la dosificación utilizando los algoritmos Alleged RC4, Verhoeff y Base 64 como se explica en la [Especificación Técnica para la generación del Código de Control](https://www.impuestos.gob.bo/ckeditor/plugins/imageuploader/uploads/356aea02e.pdf).

Este es una implementacion completa del generador y validacion del Código de Control

## Uso

``` terminal
$ pip install bolivia-cc
$ bolivia_cc --generar \
    --autorizacion=7000000006000 \
    --factura=560001 \
    --nit=3200000 \
    --fecha=2023-01-01 \
    --total=10000 \
    --llave=SECRET \
7B-F3-48-A8
```

``` python
import bolivia_cc

codigo_control = bolivia_cc.generate_control_code(
    autorizacion="20040010113",
    factura="665",
    nitci="1004141023",
    fecha="20070108",
    monto="905.23",
    llave="442F3w5AggG7644D737asd4BH5677sasdL4%44643(3C3674F4",
)

assert codigo_control == "771-D5-61-C8"
```
