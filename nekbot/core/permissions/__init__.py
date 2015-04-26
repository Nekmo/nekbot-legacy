__author__ = 'nekmo'

from nekbot.conf import settings

def get_permissions_tree(tree):
    def get_permission(perm):
        perms = [perm]
        for subperm in tree[perm]:
            perms += get_permission(subperm)
        return perms
    new_tree = {}
    for perm in tree:
        new_tree[perm] = get_permission(perm)
    return new_tree

permissions_tree = get_permissions_tree(settings.PERMISSIONS_TREE)
