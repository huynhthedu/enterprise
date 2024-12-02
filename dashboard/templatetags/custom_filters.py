from django import template

register = template.Library()

@register.filter(name='get_item')
def get_item(value, arg):
    """Get the item from a list or dictionary."""
    if isinstance(value, list):
        # If value is a list, return the item by index
        try:
            return value[int(arg)]  # arg should be the index
        except (ValueError, IndexError):
            return f"Error: Invalid index {arg}"
    elif isinstance(value, dict):
        # If value is a dictionary, return the value by key
        return value.get(arg, f"Error: Invalid key {arg}")
    return "Error: Unsupported data type"

@register.filter(name='rank_color_class')
def rank_color_class(rank):
    """Return the CSS class for the given rank."""
    if pd.isna(rank):  # Check if rank is NaN
        return 'rank-default'
        
    try:
        rank = int(rank)
    except (ValueError, TypeError):
        return 'rank-default'
    
    # Assign CSS classes based on rank ranges
    if 1 <= rank <= 10:
        print(f"Assigned rank-green to rank: {rank}")
        return 'rank-green'
    elif 11 <= rank <= 20:
        print(f"Assigned rank-light-green to rank: {rank}")
        return 'rank-light-green'
    elif 21 <= rank <= 30:
        print(f"Assigned rank-yellow to rank: {rank}")
        return 'rank-yellow'
    elif 31 <= rank <= 40:
        print(f"Assigned rank-orange to rank: {rank}")
        return 'rank-orange'
    elif 41 <= rank <= 51:
        print(f"Assigned rank-red to rank: {rank}")
        return 'rank-red'
    else:
        print(f"Assigned rank-default to rank: {rank}")
        return 'rank-default'
        
@register.filter
def get_dict_value(dictionary, key):
    """Custom filter to access dictionary keys dynamically."""
    return dictionary.get(key, '')

@register.filter
def remove_decimal(value):
    try:
        # Convert to a float and then remove decimals
        return int(float(value))
    except (ValueError, TypeError):
        return value  # In case of error, return the value as is
    
