from pyparsing import Word, nums, alphas, OneOrMore,Or, Suppress, Optional

parser = OneOrMore(Word(nums)+Suppress('*')+Word(alphas)+Suppress('^')+Word(nums) ^ Word(nums))+Suppress(Optional('+'))

raw_expressao = input('Insira a expressão: ')
