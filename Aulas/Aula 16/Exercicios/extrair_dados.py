def dados():
    tabela = """"
        <tr>
            <td style="text-align: center; border: 1px solid black">0 a 4 anos</td>
            <td style="text-align: center; border: 1px solid black">7.016.987</td>
            <td style="text-align: center; border: 1px solid black">6.779.171</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">5 a 9 anos</td>
            <td style="text-align: center; border: 1px solid black">7.624.144</td>
            <td style="text-align: center; border: 1px solid black">7.345.231</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">10 a 14 anos</td>
            <td style="text-align: center; border: 1px solid black">8.725.413</td>
            <td style="text-align: center; border: 1px solid black">8.441.348</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">15 a 19 anos</td>
            <td style="text-align: center; border: 1px solid black">8.558.868</td>
            <td style="text-align: center; border: 1px solid black">8.432.004</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">20 a 24 anos</td>
            <td style="text-align: center; border: 1px solid black">8.630.229</td>
            <td style="text-align: center; border: 1px solid black">8.614.963</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">25 a 29 anos</td>
            <td style="text-align: center; border: 1px solid black">8.460.995</td>
            <td style="text-align: center; border: 1px solid black">8.643.419</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">30 a 34 anos</td>
            <td style="text-align: center; border: 1px solid black">7.717.658</td>
            <td style="text-align: center; border: 1px solid black">8.026.854</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">35 a 39 anos</td>
            <td style="text-align: center; border: 1px solid black">6.766.664</td>
            <td style="text-align: center; border: 1px solid black">7.121.915</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">40 a 44 anos</td>
            <td style="text-align: center; border: 1px solid black">6.320.568</td>
            <td style="text-align: center; border: 1px solid black">6.688.796</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">45 a 49 anos</td>
            <td style="text-align: center; border: 1px solid black">5.692.014</td>
            <td style="text-align: center; border: 1px solid black">6.141.338</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">50 a 54 anos</td>
            <td style="text-align: center; border: 1px solid black">4.834.995</td>
            <td style="text-align: center; border: 1px solid black">5.305.407</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">55 a 59 anos</td>
            <td style="text-align: center; border: 1px solid black">3.902.344</td>
            <td style="text-align: center; border: 1px solid black">4.373.877</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">60 a 64 anos</td>
            <td style="text-align: center; border: 1px solid black">3.041.035</td>
            <td style="text-align: center; border: 1px solid black">3.468.085</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">65 a 69 anos</td>
            <td style="text-align: center; border: 1px solid black">2.224.065</td>
            <td style="text-align: center; border: 1px solid black">2.616.745</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">70 a 74 anos</td>
            <td style="text-align: center; border: 1px solid black">1.667.372</td>
            <td style="text-align: center; border: 1px solid black">2.074.264</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">75 a 79 anos</td>
            <td style="text-align: center; border: 1px solid black">1.090.517</td>
            <td style="text-align: center; border: 1px solid black">1.472.930</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">80 a 84 anos</td>
            <td style="text-align: center; border: 1px solid black">668.623</td>
            <td style="text-align: center; border: 1px solid black">998.349</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">85 a 89 anos</td>
            <td style="text-align: center; border: 1px solid black">310.759</td>
            <td style="text-align: center; border: 1px solid black">508.724</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">90 a 94 anos</td>
            <td style="text-align: center; border: 1px solid black">114.964</td>
            <td style="text-align: center; border: 1px solid black">211.594</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">95 a 99 anos</td>
            <td style="text-align: center; border: 1px solid black">31.529</td>
            <td style="text-align: center; border: 1px solid black">66.806</td>
        </tr>

        <tr>
            <td style="text-align: center; border: 1px solid black">100 anos e mais</td>
            <td style="text-align: center; border: 1px solid black">7.247</td>
            <td style="text-align: center; border: 1px solid black">16.989</td>
        </tr>
    """.split("<tr>")

    valores1 = []
    for i in tabela:
        valores1.append(i.split('<td style="text-align: center; border: 1px solid black">'))
    valores2 = []
    for i in valores1:
        if len(i) > 3: 
            valores3 = []
            valores3.append(i[1][:i[1].find(" anos")])
            valores3.append(i[2][:i[2].find("<")].replace(".", ""))
            valores3.append(i[3][:i[3].find("<")].replace(".", ""))
            valores2.append(valores3)
    
    return valores2
    