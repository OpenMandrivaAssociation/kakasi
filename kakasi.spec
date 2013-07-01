Summary:	- kanji kana simple inverter
Name:		kakasi
Version:	2.3.4
Release:	11
License:	GPL
Group:		System/Internationalization
URL:		http://kakasi.namazu.org/
Source:		http://kakasi.namazu.org/stable/kakasi-%{version}.tar.bz2

%description
KAKASI is the language processing filter to convert Kanji characters 
to Hiragana, Katakana or Romaji(1) and may be helpful to read Japanese 
documents. Word-splitting patch has merged from version 2.3.0.

%package devel
Summary:	Header file and libraries of KAKASI
Group:		Development/Other
Requires:	kakasi = %{version}-%{release}

%description devel
Header file and Libraries of KAKASI. 

%package dict
Summary:	The base dictionary of KAKASI
Group:		System/Internationalization
Provides:	kakasidict

%description dict
The basic dictionary of KAKASI.

%prep
%setup -q

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_mandir}/ja/man1
install -m 644 doc/kakasi.1 %{buildroot}%{_mandir}/ja/man1

%files
%doc AUTHORS ChangeLog COPYING NEWS README README-ja
%{_bindir}/kakasi
%{_bindir}/mkkanwa
%{_bindir}/atoc_conv
%{_bindir}/rdic_conv
%{_bindir}/wx2_conv
%{_libdir}/libkakasi.so.*
%{_mandir}/ja/man1/kakasi.1*
%{_datadir}/kakasi/itaijidict

%files devel
%{_bindir}/kakasi-config
%{_libdir}/libkakasi.so
%{_includedir}/libkakasi.h

%files dict
%{_datadir}/kakasi/kanwadict

%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 2.3.4-10mdv2011.0
+ Revision: 612521
- the mass rebuild of 2010.1 packages

* Sun Dec 13 2009 J辿r担me Brenier <incubusss@mandriva.org> 2.3.4-9mdv2010.1
+ Revision: 478049
- use %%configure2_5x

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.3.4-7mdv2009.0
+ Revision: 247489
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.3.4-5mdv2008.1
+ Revision: 140829
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - fix man pages


* Sun Jul 16 2006 Nicolas Lcureuil <neoclust@mandriva.org> 2.3.4-4mdv2007.0
- Rebuild

* Wed Apr 27 2005 Nicolas Lcureuil <neoclust@mandriva.org> 2.3.4-3mdk
- Fix MultiArch

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.3.4-2mdk
- rebuild

