def mdc_ext(a, b):

	r = a%b
	q = a//b

	if r == 0:
		return (0, 1, b)

	x, y, mdc = mdc_ext(b, r)

	return(y, x-q*y, mdc)


a = int(input())
b = int(input())

x, y, mdc = mdc_ext(a, b)

print(mdc, x, y)
