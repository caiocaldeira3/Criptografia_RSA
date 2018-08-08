def mdc_ext(a, b):

	r = a%b
	q = a//b

	if r == 0:
		return (0, 1, b)

	x, y, mdc = mdc_ext(b, r)

	return(y, x-q*y, mdc)

def inverso_modular(a, b):
	x, y, mdc = mdc_ext(a, b)
	if mdc == 1:
	    return x
    return None

a = int(input())
b = int(input())

print(inverso_modular(a, b))
