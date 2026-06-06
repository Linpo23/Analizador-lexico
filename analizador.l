%{
#include <stdio.h>
#include <string.h>

int linea = 1;
int total = 0;

void imprimir(const char *tipo, const char *lexema) {
    printf("%-15s | %-25s | linea %d\n", tipo, lexema, linea);
    total++;
}
%}

DIGITO      [0-9]
LETRA       [a-zA-Z_]
ID          {LETRA}({LETRA}|{DIGITO})*
ENTERO      {DIGITO}+
FLOAT       {DIGITO}+"."{DIGITO}+
CADENA      \"[^\"]*\"
OPERADOR    "=="|"!="|"<="|">="|"&&"|"||"|[+\-*\/=<>!%]
PUNTUACION  [(){}\[\];,.]
ESPACIO     [ \t\r]+

%%

"if"        { imprimir("KEYWORD",      yytext); }
"else"      { imprimir("KEYWORD",      yytext); }
"while"     { imprimir("KEYWORD",      yytext); }
"for"       { imprimir("KEYWORD",      yytext); }
"do"        { imprimir("KEYWORD",      yytext); }
"return"    { imprimir("KEYWORD",      yytext); }
"break"     { imprimir("KEYWORD",      yytext); }
"int"       { imprimir("KEYWORD",      yytext); }
"float"     { imprimir("KEYWORD",      yytext); }
"double"    { imprimir("KEYWORD",      yytext); }
"char"      { imprimir("KEYWORD",      yytext); }
"bool"      { imprimir("KEYWORD",      yytext); }
"void"      { imprimir("KEYWORD",      yytext); }
"string"    { imprimir("KEYWORD",      yytext); }
"true"      { imprimir("BOOLEANO",     yytext); }
"false"     { imprimir("BOOLEANO",     yytext); }
"null"      { imprimir("NULO",         yytext); }
"const"     { imprimir("KEYWORD",      yytext); }

{FLOAT}     { imprimir("FLOAT",        yytext); }
{ENTERO}    { imprimir("ENTERO",       yytext); }
{CADENA}    { imprimir("CADENA",       yytext); }
{ID}        { imprimir("IDENTIFICADOR",yytext); }
{OPERADOR}  { imprimir("OPERADOR",     yytext); }
{PUNTUACION}{ imprimir("PUNTUACION",   yytext); }

"//"[^\n]*  { /* comentario, se ignora */ }

\n          { linea++; }
{ESPACIO}   { /* espacio, se ignora */ }

.           { printf("[ERROR] caracter no reconocido: '%s' en linea %d\n", yytext, linea); }

%%

int main(int argc, char *argv[]) {
    if (argc > 1) {
        yyin = fopen(argv[1], "r");
        if (!yyin) {
            printf("No se pudo abrir el archivo.\n");
            return 1;
        }
    }

    printf("TIPO            | LEXEMA                    | UBICACION\n");
    printf("------------------------------------------------------\n");

    yylex();

    printf("------------------------------------------------------\n");
    printf("Total de tokens: %d\n", total);
    return 0;
}

int yywrap() { return 1; }
