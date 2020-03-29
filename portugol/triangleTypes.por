/*Fazer um algoritmo para ler os três lados de um triângulo, 
 * dizer se ele é isósceles, 
 * escaleno ou equilátero.
 * OBS: Antes de verificar o tipo do triângulo deve-se verificar 
 * se os ladosfornecidos formam triângulo ( L1+L2 > L3; L2+L3 >L1 e L3+L1 > L2)
 * 
 * 1. Criar as variáveis para os 3 lados atribuindo valores
 * 2. Verificar se é triangulo utilizando expressão disponibilizada
 * 3. Verificar se todos os lados são iguais e imprimir equilátero caso verdadeiro
 * 4. Verificar se todos os lados são diferentes e imprimir escaleno caso verdadeiro
 * 5. imprimir isóceles se não for nenhum anterior
 */

programa
{
	
	funcao inicio()
	{
		real ladoUm = 14;
		real ladoDois = 14;
		real ladoTres = 14;

		se(ladoUm + ladoDois > ladoTres e ladoUm + ladoTres > ladoDois e ladoDois + ladoTres > ladoUm) {
			se(ladoUm == ladoDois e ladoUm == ladoTres e ladoDois == ladoTres) {
				escreva("É um triângulo equilátero!"); 
			} senao se (ladoUm != ladoDois e ladoUm != ladoTres e ladoDois != ladoTres) {
				escreva("É um triângulo Escaleno!"); 
			} senao {
				escreva("É um triângulo Isóceles!"); 
			}
		} senao {
			escreva("Não é um triângulo");
		}
	}
}
/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 716; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */