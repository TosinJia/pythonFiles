
def damage(skill1, skill2):
    damage1 = skill1*2
    damage2 = skill2*3+1
    return damage1, damage2


# 多个返回值会组装成一个元组返回
damages = damage(2, 3)
print(type(damages))
print(damages[0], damages[1])

# 序列解包
skill1_damage, skill2_damage2 = damage(2, 3)
print(skill1_damage, skill2_damage2)

