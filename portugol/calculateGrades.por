/* Fazer um algoritmo para ler três notas, imprimir a maior delas e a média destas notas.
 * 
 * 1. Criar variáveis para receber o valor inputado
 * 2. Criar prompt para receber as três notas
 * 3. Criar lista com valores das notas
 * 4. Criar funcao chamada verificarMaior que receba três valores
 * 5. Verificar condições entre os três números, comparando dois a dois e retornando o maior (como?)
 * 6. Criar função que recebe três parâmetros e calcula médica entre os três valores;
 */

programa
{
	
	funcao inicio() {
		real notaUm;
		real notaDois;
		real notaTres;
		
		escreva("Insira nota um: ");
		leia(notaUm);

		escreva("Insira nota dois: ");
		leia(notaDois);

		escreva("Insira nota três: ");
		leia(notaTres);

		escreva(verificarMaior(notaUm, notaDois, notaTres));
		escreva(calcularMedia(notaUm, notaDois, notaTres));
	}

	funcao real verificarMaior(real valorUm, real valorDois, real valorTres) {
		
	}

	funcao real calcularMedia(real valorUm, real valorDois, real valorTres) {
		retorne (valorUm + valorDois + valorTres) / 3;
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 917; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */