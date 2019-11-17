def clip(text : str, max_len : 'int > 0' = 80) -> str:
    """在max_len前面或后面的第一个空格处截断文本 
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)       # 返回字符串最后一次出现的位置，没有则返回-1 
            if space_after >= 0:
                end = space_after
    if end is None:        # 没找到空格
        end = len(text)
    return text[:end].rstrip()        # 删除字符串末尾指定的字符串，默认为空格


print(clip.__annotations__)