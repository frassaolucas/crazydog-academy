/* Faça um algoritmo que permita ao usuário fornecer três números e escolhere ntre as opções: 
 * calcular a média, calcular a soma ou calcular a multiplicação dos números.
 * 
 * 1. Criar três variáveis para os números;
 * 2. Criar uma variável para a operação desejada;
 * 3. Coletar os valores das quatro variáveis;
 * 4. Criar função soma que receba três parâmetros;
 * 5. Criar função multiplicação que receba três parâmtros;
 * 6. Criar função média que receba três parâmetros;
 * 7. Criar condicional para verificar qual opção de operação foi inputada;
 * 8. Disparar função de acordo com o valor inputado da operação, passando os valores como parâmetro;
 */

programa
{
	
	funcao inicio() {
		real numeroUm;
		real numeroDois;
		real numeroTres;
		cadeia operacaoMatematica;
		
		escreva("Insira número um: ");
		leia(numeroUm);

		escreva("Insira numero dois: ");
		leia(numeroDois);

		escreva("Insira numero três: ");
		leia(numeroTres);

		escreva("Qual operação matemática deseja realizar: média, soma ou multiplicação? ");
		leia(operacaoMatematica);

		se(operacaoMatematica == "média") {
			escreva(calcularMedia(numeroUm, numeroDois, numeroTres));
		} senao se (operacaoMatematica == "soma") {
			escreva(calcularSoma(numeroUm, numeroDois, numeroTres));
		} senao se (operacaoMatematica == "multiplicação") {
			escreva(calcularMultiplicacao(numeroUm, numeroDois, numeroTres));
		}
	}

	funcao real calcularMedia(real valorUm, real valorDois, real valorTres) {
		retorne ((valorUm + valorDois + valorTres) / 3);
	}

	funcao real calcularSoma(real valorUm, real valorDois, real valorTres) {
		retorne valorUm + valorDois + valorTres;
	}

	funcao real calcularMultiplicacao(real valorUm, real valorDois, real valorTres) {
		retorne valorUm * valorDois * valorTres;
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 949; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */