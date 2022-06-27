a, b, c, d, e = 1, 4, 7, 8, 4
print(f'nilai sebelum : a={a} b={b} c={c} d={d} e={e}')
#A formatted string literal or f-string is a string literal that is prefixed with 'f' or 'F'. These strings may contain replacement fields,
# which are expressions delimited by curly braces {}. While other string literals always have a constant value, formatted strings are really
# expressions evaluated at run time.
a, b, c, d, e = b, c, d, e, a
print(f'nilai sesudah : a={a} b={b} c={c} d={d} e={e}')