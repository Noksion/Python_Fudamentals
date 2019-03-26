to_do = ['cooking', 'workout', 'python', 'hugs']
done = []

while to_do:
    verify = to_do.pop()
    print('Verifying ' + verify.title() + "...")
    done.append(verify)

print('\nThe following actions were successfully performed: ')
for i in done:
    print(' - ' + i.title())
