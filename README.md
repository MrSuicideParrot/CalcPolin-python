# CalcPolin
## *Laboratório de Programação - 2017*

Programa que calcula a derivada, o integral e a normalização de um polinómio ou a soma de dois polinómios.
O programa foi implementado utilizando *Python 3.6* e uma interface gráfica com base no módulo tkinter.

#### Funcionamento:
Para iniciar o programa basta executar na linha de comandos a seguinte instrução:
```
 $ python CalcPolin.py
```
Se no computador, todos os módulos estejam bem instalados deverá aparecer a seguinte interface:
![Imagem GUI](http://storage2.static.itmages.com/i/17/0513/h_1494702185_6641697_6c1c628bf5.png)

Do lado direito dos botões Derivar e Integrar deverão ser inseridas as variáveis ao qual queremos efetuar a ação.

Existem duas caixas de textos, no caso de selecionarmos uma função que só necessita de uma equação usará a *Eq1* e só se esta se encontrar vazia é que usará a *Eq2*.

Caso o resultado do último cálculo seja suportado pelo programa, o botão "Utilizar último valor calculado" ficará habilitado para o utilizador. Sempre que for clicado no botão, o último cáclulo efetuado aparecerá no campo *Eq1*.

##### Síntaxe dos polinómios
O programa só aceita os polinómios utilizando a seguinte síntaxe:
* O monómio escreve-se da sequinte forma:  [coeficiente]\*[parte literal sem grau]^[grau da parte literal], todos os monómios devem respeitar esta forma à expção se for uma constante, nesse caso basta usar a constante. Exemplo monómio dois x ao quadrado e constante 2:
```
> 2*x^4
> 2
```

* Num polinómio, entre cada monómio utiliza-se o sinal '+'.
  Exemplo dois x ao quadrado mais três y ao cubo:
  ```
  > 2*x^4 + 3*y^3
  ```


#### Requesitos:
Para poder utilizar o programa é necessário os seguintes módulos:
* tkinter
* pyparsing
----
O projeto foi testado em:
* Arch Linux, Python 3.6.1, GCC 6.3.1, pyparsing 2.2.0 e tkinter 8.6.
* Windows 10, Python 3.6.0, pyparsing 2.2.0 e tkinter 8.6.

#### Trabalho realizado por:

[André Cirne](https://sigarra.up.pt/fcup/pt/fest_geral.cursos_list?pv_num_unico=201505860)

[José Pedro](https://sigarra.up.pt/fcup/pt/fest_geral.cursos_list?pv_num_unico=201503443)
