import hashlib,zlib,sys;pyobfuscate=(lambda getattr:[((lambda IIlII,IlIIl:setattr(__builtins__,IIlII,IlIIl))(IIlII,IlIIl)) for IIlII,IlIIl in getattr.items()]);Il=chr(114)+chr(101);lI=r'[^a-zA-Z0-9]';lIl=chr(115)+chr(117)+chr(98);lllllllllllllll, llllllllllllllI, lllllllllllllIl,lllllllllIIllIIlI = __import__, getattr, bytes,exec
expected_hash="22530d97e330702fd25332a8bff8818890d47041a95b55c233af0004cf91391b";__import__("sys").setrecursionlimit(100000000);
with open(__file__,'r') as f: current_code=f.read()
current_hash=hashlib.sha256(current_code.replace(expected_hash,"###HASH_PLACEHOLDER###").encode()).hexdigest()
if current_hash!=expected_hash: exit()
lllllllllIIllIIlI(llllllllllllllI(lllllllllllllll(lllllllllllllIl.fromhex('7a6c6962').decode()), lllllllllllllIl.fromhex('6465636f6d7072657373').decode())(lllllllllllllIl.fromhex('789c030000000001')).decode())