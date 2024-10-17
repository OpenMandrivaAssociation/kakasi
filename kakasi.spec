Summary:	KAKASI - kanji kana simple inverter
Name:		kakasi
Version:	2.3.4
Release:	13
License:	GPL
Group:		System/Internationalization
URL:		https://kakasi.namazu.org/
Source:		http://kakasi.namazu.org/stable/kakasi-%{version}.tar.gz

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

