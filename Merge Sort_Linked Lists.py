def merge_sort(linked_list):
    """
Classifica uma lista encadeada em ordem crescente
     - Divide recursivamente a lista encadeada em sublistas contendo um único nó
     - Reúne as sublistas repetidamente para produzir sublistas ordenadas até que uma permaneça

     Retorna uma lista encadeada ordenada

     Executa em tempo  O (n log n)
     Ocupa espaço de O (n)
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    """
Divide a lista não classificada no ponto médio em sublistas
     Executa em tempo O (log n)
    """
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half


def merge(left, right):
    """
Merge duas listas encadeadas, ordenando por dados em nós
     Retorna uma nova lista merged
     Ocupa espaço O (n)
     Executa em tempo O (n)
    """

    # Crie uma nova lista encadeada que contém os nós da mistura do esquerdo e direito 
    merged = LinkedList()
    # Adicione um head falso que será descartada depois. 
    merged.add(0)
    # Definir current (atual) como o head  da lista encadeada 
    current = merged.head

    # Obtem os nós head  para as listas encadeadas à esquerda e à direita 
    left_head = left.head
    right_head = right.head

     # Itera sobre a esquerda e a direita até o nó tail de ambos
     # esquerda e direita
    while left_head or right_head:
    # Se o nó head da esquerda for None , estamos no Tail
    # Adicione o nó Tail da direita para a lista encadeada merged
        if left_head is None:
            current.next_node = right_head
            # Chame próximo à direita para definir a condição do loop como False 
            right_head = right_head.next_node 
        # Se o nó principal da direita for None, estamos no Tail
        # Adicione o nó Tail da esquerda para a lista encadeada merged
        elif right_head is None:
            current.next_node = left_head
            # Chame próximo à esquerda para definir a condição do loop como False
            left_head = left_head.next_node
        else:
            # Not  em nenhum dos nós da cauda
            # Obtenha dados do nó para realizar operações de comparação 
            left_data = left_head.data
            right_data = right_head.data

            # Se os dados à esquerda forem menores que à direita, defina o nó current (atual) para left
            # Mova left head para next node, o próximo nó 
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            # Se os dados à esquerda forem maiores do que à direita, defina o nó atual para a right
            # Mova right head para  next node, o próximo nó 
            else:
                current.next_node = right_head
                right_head = right_head.next_node

        # Move current (atual) para next node
        current = current.next_node

    # Descartar o head falso e definir o primeiro nó merged como Head  
    head = merged.head.next_node
    merged.head = head

    return merged