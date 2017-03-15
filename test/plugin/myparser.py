import re
import sys
sys.path.append('/home/varsha/.vim/bundle/test/plugin')
sys.path.append('..')
#from myparser import clex.py
#import importlib.util
#spec = importlib.util.spec_from_file_location("myparser", "/home/varsha/.vim/bundle/test/plugin/myparser")
#clex = importlib.util.module_from_spec(spec)
import vim
import clex
#import clex
import string
# Get the token map
tokens = clex.tokens

start = 'translation_unit'
('tokens = ', "['ID', 'CONSTANT', 'STRING_LITERAL', 'SIZEOF', 'PTR_OP', 'INC_OP', 'DEC_OP', 'LEFT_OP', 'RIGHT_OP', 'LE_OP', 'GE_OP', 'EQ_OP', 'NE_OP', 'AND_OP', 'OR_OP', 'MUL_ASSIGN', 'DIV_ASSIGN', 'MOD_ASSIGN', 'ADD_ASSIGN', 'SUB_ASSIGN', 'LEFT_ASSIGN', 'RIGHT_ASSIGN', 'AND_ASSIGN', 'XOR_ASSIGN', 'OR_ASSIGN', 'TYPE_NAME', 'TYPEDEF', 'EXTERN', 'STATIC', 'AUTO', 'REGISTER', 'CHAR', 'SHORT', 'INT', 'LONG', 'SIGNED', 'UNSIGNED', 'FLOAT', 'DOUBLE', 'CONST', 'VOLATILE', 'VOID', 'STRUCT', 'UNION', 'ENUM', 'ELLIPSIS', 'CASE', 'DEFAULT', 'IF', 'ELSE', 'SWITCH', 'WHILE', 'DO', 'FOR', 'GOTO', 'CONTINUE', 'BREAK', 'RETURN']")
()
('precedence = ', '[]')
()
# -------------- RULES ----------------
()
def p_primary_expression_1(p):
    '''primary_expression : ID'''
()
def p_primary_expression_2(p):
    '''primary_expression : INT_CONST_DEC'''
()
def p_primary_expression_3(p):
    '''primary_expression : STRING_LITERAL'''
()
def p_primary_expression_4(p):
    '''primary_expression : LPAREN expression RPAREN'''
()
def p_postfix_expression_1(p):
    '''postfix_expression : primary_expression'''
()
def p_postfix_expression_2(p):
    '''postfix_expression : postfix_expression LSQUARE expression RSQUARE'''
()
def p_postfix_expression_3(p):
    '''postfix_expression : postfix_expression LPAREN RPAREN'''
()
def p_postfix_expression_4(p):
    '''postfix_expression : postfix_expression LPAREN argument_expression_list RPAREN'''
()
def p_postfix_expression_5(p):
    '''postfix_expression : postfix_expression DOT ID'''
()
def p_postfix_expression_6(p):
    '''postfix_expression : postfix_expression PTR_OP ID'''
()
def p_postfix_expression_7(p):
    '''postfix_expression : postfix_expression INC'''
()
def p_postfix_expression_8(p):
    '''postfix_expression : postfix_expression DEC'''
()
def p_argument_expression_list_1(p):
    '''argument_expression_list : assignment_expression'''
()
def p_argument_expression_list_2(p):
    '''argument_expression_list : argument_expression_list COMMA assignment_expression'''
()
def p_unary_expression_1(p):
    '''unary_expression : postfix_expression'''
()
def p_unary_expression_2(p):
    '''unary_expression : INC unary_expression'''
()
def p_unary_expression_3(p):
    '''unary_expression : DEC unary_expression'''
()
def p_unary_expression_4(p):
    '''unary_expression : unary_operator cast_expression'''
()
def p_unary_expression_5(p):
    '''unary_expression : SIZEOF unary_expression'''
()
def p_unary_expression_6(p):
    '''unary_expression : SIZEOF LPAREN type_name RPAREN'''
()
def p_unary_operator_1(p):
    '''unary_operator : BAND'''
()
def p_unary_operator_2(p):
    '''unary_operator : TIMES'''
()
def p_unary_operator_3(p):
    '''unary_operator : PLUS'''
()
def p_unary_operator_4(p):
    '''unary_operator : MINUS'''
()
def p_unary_operator_5(p):
    '''unary_operator : BNOT'''
()
def p_unary_operator_6(p):
    '''unary_operator : LNOT'''
()
def p_cast_expression_1(p):
    '''cast_expression : unary_expression'''
()
def p_cast_expression_2(p):
    '''cast_expression : LPAREN type_name RPAREN cast_expression'''
()
def p_multiplicative_expression_1(p):
    '''multiplicative_expression : cast_expression'''
()
def p_multiplicative_expression_2(p):
    '''multiplicative_expression : multiplicative_expression TIMES cast_expression'''
()
def p_multiplicative_expression_3(p):
    '''multiplicative_expression : multiplicative_expression DIVIDE cast_expression'''
()
def p_multiplicative_expression_4(p):
    '''multiplicative_expression : multiplicative_expression MOD cast_expression'''
()
def p_additive_expression_1(p):
    '''additive_expression : multiplicative_expression'''
()
def p_additive_expression_2(p):
    '''additive_expression : additive_expression PLUS multiplicative_expression'''
()
def p_additive_expression_3(p):
    '''additive_expression : additive_expression MINUS multiplicative_expression'''
()
def p_shift_expression_1(p):
    '''shift_expression : additive_expression'''
()
def p_shift_expression_2(p):
    '''shift_expression : shift_expression LSHIFT additive_expression'''
()
def p_shift_expression_3(p):
    '''shift_expression : shift_expression RSHIFT additive_expression'''
()
def p_relational_expression_1(p):
    '''relational_expression : shift_expression'''
()
def p_relational_expression_2(p):
    '''relational_expression : relational_expression LT shift_expression'''
()
def p_relational_expression_3(p):
    '''relational_expression : relational_expression GT shift_expression'''
()
def p_relational_expression_4(p):
    '''relational_expression : relational_expression LEQ shift_expression'''
()
def p_relational_expression_5(p):
    '''relational_expression : relational_expression GEQ shift_expression'''
()
def p_equality_expression_1(p):
    '''equality_expression : relational_expression'''
()
def p_equality_expression_2(p):
    '''equality_expression : equality_expression EQ relational_expression'''
()
def p_equality_expression_3(p):
    '''equality_expression : equality_expression NEQ relational_expression'''
()
def p_and_expression_1(p):
    '''and_expression : equality_expression'''
()
def p_and_expression_2(p):
    '''and_expression : and_expression BAND equality_expression'''
()
def p_exclusive_or_expression_1(p):
    '''exclusive_or_expression : and_expression'''
()
def p_exclusive_or_expression_2(p):
    '''exclusive_or_expression : exclusive_or_expression XOR and_expression'''
()
def p_inclusive_or_expression_1(p):
    '''inclusive_or_expression : exclusive_or_expression'''
()
def p_inclusive_or_expression_2(p):
    '''inclusive_or_expression : inclusive_or_expression BOR exclusive_or_expression'''
()
def p_logical_and_expression_1(p):
    '''logical_and_expression : inclusive_or_expression'''
()
def p_logical_and_expression_2(p):
    '''logical_and_expression : logical_and_expression LAND inclusive_or_expression'''
()
def p_logical_or_expression_1(p):
    '''logical_or_expression : logical_and_expression'''
()
def p_logical_or_expression_2(p):
    '''logical_or_expression : logical_or_expression LOR logical_and_expression'''
()
def p_conditional_expression_1(p):
    '''conditional_expression : logical_or_expression'''
()
def p_conditional_expression_2(p):
    '''conditional_expression : logical_or_expression IS_TRUE expression COLON conditional_expression'''
()
def p_assignment_expression_1(p):
    '''assignment_expression : conditional_expression'''
()
def p_assignment_expression_2(p):
    '''assignment_expression : unary_expression assignment_operator assignment_expression'''
()
def p_assignment_operator_1(p):
    '''assignment_operator : ASSIGN'''
()
def p_assignment_operator_2(p):
    '''assignment_operator : MUL_ASSIGN'''
()
def p_assignment_operator_3(p):
    '''assignment_operator : DIV_ASSIGN'''
()
def p_assignment_operator_4(p):
    '''assignment_operator : MOD_ASSIGN'''
()
def p_assignment_operator_5(p):
    '''assignment_operator : ADD_ASSIGN'''
()
def p_assignment_operator_6(p):
    '''assignment_operator : SUB_ASSIGN'''
()
def p_assignment_operator_7(p):
    '''assignment_operator : LSHIFT_ASSIGN'''
()
def p_assignment_operator_8(p):
    '''assignment_operator : RSHIFT_ASSIGN'''
()
def p_assignment_operator_9(p):
    '''assignment_operator : AND_ASSIGN'''
()
def p_assignment_operator_10(p):
    '''assignment_operator : XOR_ASSIGN'''
()
def p_assignment_operator_11(p):
    '''assignment_operator : OR_ASSIGN'''
()
def p_expression_1(p):
    '''expression : assignment_expression'''
()
def p_expression_2(p):
    '''expression : expression COMMA assignment_expression'''
()
def p_constant_expression_1(p):
    '''constant_expression : conditional_expression'''
()
def p_declaration_1(p):
    '''declaration : declaration_specifiers SEMICOLON'''
()
def p_declaration_2(p):
    '''declaration : declaration_specifiers init_declarator_list SEMICOLON'''
()
def p_declaration_specifiers_1(p):
    '''declaration_specifiers : storage_class_specifier'''
()
def p_declaration_specifiers_2(p):
    '''declaration_specifiers : storage_class_specifier declaration_specifiers'''
()
def p_declaration_specifiers_3(p):
    '''declaration_specifiers : type_specifier'''
()
def p_declaration_specifiers_4(p):
    '''declaration_specifiers : type_specifier declaration_specifiers'''
()
def p_declaration_specifiers_5(p):
    '''declaration_specifiers : type_qualifier'''
()
def p_declaration_specifiers_6(p):
    '''declaration_specifiers : type_qualifier declaration_specifiers'''
()
def p_init_declarator_list_1(p):
    '''init_declarator_list : init_declarator'''
()
def p_init_declarator_list_2(p):
    '''init_declarator_list : init_declarator_list COMMA init_declarator'''
()
def p_init_declarator_1(p):
    '''init_declarator : declarator'''
()
def p_init_declarator_2(p):
    '''init_declarator : declarator ASSIGN initializer'''
()
def p_storage_class_specifier_1(p):
    '''storage_class_specifier : TYPEDEF'''
()
def p_storage_class_specifier_2(p):
    '''storage_class_specifier : EXTERN'''
()
def p_storage_class_specifier_3(p):
    '''storage_class_specifier : STATIC'''
()
def p_storage_class_specifier_4(p):
    '''storage_class_specifier : AUTO'''
()
def p_storage_class_specifier_5(p):
    '''storage_class_specifier : REGISTER'''
()
def p_type_specifier_1(p):
    '''type_specifier : VOID'''
()
def p_type_specifier_2(p):
    '''type_specifier : CHAR'''
()
def p_type_specifier_3(p):
    '''type_specifier : SHORT'''
()
def p_type_specifier_4(p):
    '''type_specifier : INT'''
()
def p_type_specifier_5(p):
    '''type_specifier : LONG'''
()
def p_type_specifier_6(p):
    '''type_specifier : FLOAT'''
()
def p_type_specifier_7(p):
    '''type_specifier : DOUBLE'''
()
def p_type_specifier_8(p):
    '''type_specifier : SIGNED'''
()
def p_type_specifier_9(p):
    '''type_specifier : UNSIGNED'''
()
def p_type_specifier_10(p):
    '''type_specifier : struct_or_union_specifier'''
()
def p_type_specifier_11(p):
    '''type_specifier : enum_specifier'''
()
def p_struct_or_union_specifier_1(p):
    '''struct_or_union_specifier : struct_or_union ID LBRACE struct_declaration_list RBRACE'''
()
def p_struct_or_union_specifier_2(p):
    '''struct_or_union_specifier : struct_or_union LBRACE struct_declaration_list RBRACE'''
()
def p_struct_or_union_specifier_3(p):
    '''struct_or_union_specifier : struct_or_union ID'''
()
def p_struct_or_union_1(p):
    '''struct_or_union : STRUCT'''
()
def p_struct_or_union_2(p):
    '''struct_or_union : UNION'''
()
def p_struct_declaration_list_1(p):
    '''struct_declaration_list : struct_declaration'''
()
def p_struct_declaration_list_2(p):
    '''struct_declaration_list : struct_declaration_list struct_declaration'''
()
def p_struct_declaration_1(p):
    '''struct_declaration : specifier_qualifier_list struct_declarator_list SEMICOLON'''
()
def p_specifier_qualifier_list_1(p):
    '''specifier_qualifier_list : type_specifier specifier_qualifier_list'''
()
def p_specifier_qualifier_list_2(p):
    '''specifier_qualifier_list : type_specifier'''
()
def p_specifier_qualifier_list_3(p):
    '''specifier_qualifier_list : type_qualifier specifier_qualifier_list'''
()
def p_specifier_qualifier_list_4(p):
    '''specifier_qualifier_list : type_qualifier'''
()
def p_struct_declarator_list_1(p):
    '''struct_declarator_list : struct_declarator'''
()
def p_struct_declarator_list_2(p):
    '''struct_declarator_list : struct_declarator_list COMMA struct_declarator'''
()
def p_struct_declarator_1(p):
    '''struct_declarator : declarator'''
()
def p_struct_declarator_2(p):
    '''struct_declarator : COLON constant_expression'''
()
def p_struct_declarator_3(p):
    '''struct_declarator : declarator COLON constant_expression'''
()
def p_enum_specifier_1(p):
    '''enum_specifier : ENUM LBRACE enumerator_list RBRACE'''
()
def p_enum_specifier_2(p):
    '''enum_specifier : ENUM ID LBRACE enumerator_list RBRACE'''
()
def p_enum_specifier_3(p):
    '''enum_specifier : ENUM ID'''
()
def p_enumerator_list_1(p):
    '''enumerator_list : enumerator'''
()
def p_enumerator_list_2(p):
    '''enumerator_list : enumerator_list COMMA enumerator'''
()
def p_enumerator_1(p):
    '''enumerator : ID'''
()
def p_enumerator_2(p):
    '''enumerator : ID ASSIGN constant_expression'''
()
def p_type_qualifier_1(p):
    '''type_qualifier : CONST'''
()
def p_type_qualifier_2(p):
    '''type_qualifier : VOLATILE'''
()
def p_declarator_1(p):
    '''declarator : pointer direct_declarator'''
()
def p_declarator_2(p):
    '''declarator : direct_declarator'''
()
def p_direct_declarator_1(p):
    '''direct_declarator : ID'''
()
def p_direct_declarator_2(p):
    '''direct_declarator : LPAREN declarator RPAREN'''
()
def p_direct_declarator_3(p):
    '''direct_declarator : direct_declarator '[' constant_expression RSQUARE'''
()
def p_direct_declarator_4(p):
    '''direct_declarator : direct_declarator '[' RSQUARE'''
()
def p_direct_declarator_5(p):
    '''direct_declarator : direct_declarator LPAREN parameter_type_list RPAREN'''
()
def p_direct_declarator_6(p):
    '''direct_declarator : direct_declarator LPAREN identifier_list RPAREN'''
()
def p_direct_declarator_7(p):
    '''direct_declarator : direct_declarator LPAREN RPAREN'''
()
def p_pointer_1(p):
    '''pointer : TIMES'''
()
def p_pointer_2(p):
    '''pointer : '*' type_qualifier_list'''
()
def p_pointer_3(p):
    '''pointer : '*' pointer'''
()
def p_pointer_4(p):
    '''pointer : '*' type_qualifier_list pointer'''
()
def p_type_qualifier_list_1(p):
    '''type_qualifier_list : type_qualifier'''
()
def p_type_qualifier_list_2(p):
    '''type_qualifier_list : type_qualifier_list type_qualifier'''
()
def p_parameter_type_list_1(p):
    '''parameter_type_list : parameter_list'''
()
def p_parameter_type_list_2(p):
    '''parameter_type_list : parameter_list COMMA ELLIPSIS'''
()
def p_parameter_list_1(p):
    '''parameter_list : parameter_declaration'''
()
def p_parameter_list_2(p):
    '''parameter_list : parameter_list COMMA parameter_declaration'''
()
def p_parameter_declaration_1(p):
    '''parameter_declaration : declaration_specifiers declarator'''
()
def p_parameter_declaration_2(p):
    '''parameter_declaration : declaration_specifiers abstract_declarator'''
()
def p_parameter_declaration_3(p):
    '''parameter_declaration : declaration_specifiers'''
()
def p_identifier_list_1(p):
    '''identifier_list : ID'''
()
def p_identifier_list_2(p):
    '''identifier_list : identifier_list COMMA ID'''
()
def p_type_name_1(p):
    '''type_name : specifier_qualifier_list'''
()
def p_type_name_2(p):
    '''type_name : specifier_qualifier_list abstract_declarator'''
()
def p_abstract_declarator_1(p):
    '''abstract_declarator : pointer'''
()
def p_abstract_declarator_2(p):
    '''abstract_declarator : direct_abstract_declarator'''
()
def p_abstract_declarator_3(p):
    '''abstract_declarator : pointer direct_abstract_declarator'''
()
def p_direct_abstract_declarator_1(p):
    '''direct_abstract_declarator : LPAREN abstract_declarator RPAREN'''
()
def p_direct_abstract_declarator_2(p):
    '''direct_abstract_declarator : '[' RSQUARE'''
()
def p_direct_abstract_declarator_3(p):
    '''direct_abstract_declarator : '[' constant_expression RSQUARE'''
()
def p_direct_abstract_declarator_4(p):
    '''direct_abstract_declarator : direct_abstract_declarator '[' RSQUARE'''
()
def p_direct_abstract_declarator_5(p):
    '''direct_abstract_declarator : direct_abstract_declarator '[' constant_expression RSQUARE'''
()
def p_direct_abstract_declarator_6(p):
    '''direct_abstract_declarator : LPAREN RPAREN'''
()
def p_direct_abstract_declarator_7(p):
    '''direct_abstract_declarator : LPAREN parameter_type_list RPAREN'''
()
def p_direct_abstract_declarator_8(p):
    '''direct_abstract_declarator : direct_abstract_declarator LPAREN RPAREN'''
()
def p_direct_abstract_declarator_9(p):
    '''direct_abstract_declarator : direct_abstract_declarator LPAREN parameter_type_list RPAREN'''
()
def p_initializer_1(p):
    '''initializer : assignment_expression'''
()
def p_initializer_2(p):
    '''initializer : LBRACE initializer_list RBRACE'''
()
def p_initializer_3(p):
    '''initializer : LBRACE initializer_list COMMA RBRACE'''
()
def p_initializer_list_1(p):
    '''initializer_list : initializer'''
()
def p_initializer_list_2(p):
    '''initializer_list : initializer_list COMMA initializer'''
()
def p_statement_1(p):
    '''statement : labeled_statement'''
()
def p_statement_2(p):
    '''statement : compound_statement'''
()
def p_statement_3(p):
    '''statement : expression_statement'''
()
def p_statement_4(p):
    '''statement : selection_statement'''
()
def p_statement_5(p):
    '''statement : iteration_statement'''
()
def p_statement_6(p):
    '''statement : jump_statement'''
()
def p_labeled_statement_1(p):
    '''labeled_statement : ID COLON statement'''
()
def p_labeled_statement_2(p):
    '''labeled_statement : CASE constant_expression COLON statement'''
()
def p_labeled_statement_3(p):
    '''labeled_statement : DEFAULT COLON statement'''
()
def p_compound_statement_1(p):
    '''compound_statement : LBRACE RBRACE'''
()
def p_compound_statement_2(p):
    '''compound_statement : LBRACE statement_list RBRACE'''
()
def p_compound_statement_3(p):
    '''compound_statement : LBRACE declaration_list RBRACE'''
()
def p_compound_statement_4(p):
    '''compound_statement : LBRACE declaration_list statement_list RBRACE'''
()
def p_declaration_list_1(p):
    '''declaration_list : declaration'''
()
def p_declaration_list_2(p):
    '''declaration_list : declaration_list declaration'''
()
def p_statement_list_1(p):
    '''statement_list : statement'''
()
def p_statement_list_2(p):
    '''statement_list : statement_list statement'''
()
def p_expression_statement_1(p):
    '''expression_statement : SEMICOLON'''
()
def p_expression_statement_2(p):
    '''expression_statement : expression SEMICOLON'''
()
def p_selection_statement_1(p):
    '''selection_statement : IF LPAREN expression RPAREN statement'''
()
#
#def p_selection_statement_2(p):
#    '''selection_statement : IF LPAREN expression RPAREN statement ELSE statement'''
#()
def p_selection_statement_3(p):
    '''selection_statement : SWITCH LPAREN expression RPAREN statement'''
()
def p_iteration_statement_1(p):
    '''iteration_statement : WHILE LPAREN expression RPAREN statement'''
()
def p_iteration_statement_2(p):
    '''iteration_statement : DO statement WHILE LPAREN expression RPAREN SEMICOLON'''
()
def p_iteration_statement_3(p):
    '''iteration_statement : FOR LPAREN expression_statement expression_statement RPAREN statement'''
()
def p_iteration_statement_4(p):
    '''iteration_statement : FOR LPAREN expression_statement expression_statement expression RPAREN statement'''
()
def p_jump_statement_1(p):
    '''jump_statement : GOTO ID SEMICOLON'''
()
def p_jump_statement_2(p):
    '''jump_statement : CONTINUE SEMICOLON'''
()
def p_jump_statement_3(p):
    '''jump_statement : BREAK SEMICOLON'''
()
def p_jump_statement_4(p):
    '''jump_statement : RETURN SEMICOLON'''
()
def p_jump_statement_5(p):
    '''jump_statement : RETURN expression SEMICOLON'''
()
def p_translation_unit_1(p):
    '''translation_unit : external_declaration'''
()
def p_translation_unit_2(p):
    '''translation_unit : translation_unit external_declaration'''
()
def p_external_declaration_1(p):
    '''external_declaration : function_definition'''
()
def p_external_declaration_2(p):
    '''external_declaration : declaration'''
()
def p_function_definition_1(p):
    '''function_definition : declaration_specifiers declarator declaration_list compound_statement'''
()
def p_function_definition_2(p):
    '''function_definition : declaration_specifiers declarator compound_statement'''
()
def p_function_definition_3(p):
    '''function_definition : declarator declaration_list compound_statement'''
()
def p_function_definition_4(p):
    '''function_definition : declarator compound_statement'''
()
# -------------- RULES END ----------------
# 
# #include <stdio.h>
# 
# extern char yytext[];
# extern int column;
# 
# yyerror(s)
# char *s;
# {
#     fflush(stdout);
#     printf("\n%*s\n%*s\n", column, "^", column, s);
# }

if __name__ == '__main__':
    from ply import *
    #yacc.yacc()

    yacc.yacc(method='LALR',write_tables=True,debug=True)
    #filename = sys.argv[1]
    #f = open(filename)
    data = string.join(vim.current.buffer, "\n")
    print type(data)
    #f.read() 
    #string.join(vim.current.buffer, "\n")
    #f.close()
    yacc.parse(data)
