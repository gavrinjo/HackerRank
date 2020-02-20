n = int(8)

print(bin(n)[2::])
print(hex(n)[2::].upper())
print(oct(n)[2::])


nums = ([f"{x} {oct(x)[2::]} {hex(x)[2::].upper()} {bin(x)[2::]}" for x in range(n)])
print("\n".join(nums))

for i in range(n):
    b = bin(i)[2::].rjust(len(bin(n)[2::]), " ")
    h = hex(i)[2::].upper().rjust(len(bin(n)[2::]), " ")
    o = oct(i)[2::].rjust(len(bin(n)[2::]), " ")
    print(f"{i} {h} {o} {b}")
