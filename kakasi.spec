%define  version 2.3.4
%define  release %mkrel 10

Summary: KAKASI - kanji kana simple inverter
Name: kakasi
Version: %{version}
Release: %{release}
Source: http://kakasi.namazu.org/stable/kakasi-%{version}.tar.bz2
URL: http://kakasi.namazu.org/
License: GPL
Group: System/Internationalization
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
KAKASI is the language processing filter to convert Kanji characters 
to Hiragana, Katakana or Romaji(1) and may be helpful to read Japanese 
documents. Word-splitting patch has merged from version 2.3.0.

%description -l ja
KAKASI は漢字かなまじり文をひらがな文やローマ字文に変換することを
目的として作成したプログラムと辞書の総称です。さらに、バージョン 
2.3.0 からは、分かち書きパッチがマージされました。

%package devel
Summary: Header file and libraries of KAKASI
Group: Development/Other
Requires: kakasi = %{version}

%description devel
Header file and Libraries of KAKASI. 

%description devel -l ja
KAKASIのヘッダファイル及びライブラリです。

%package dict
Summary: The base dictionary of KAKASI
Group: System/Internationalization
Obsoletes: kakasidict
Provides: kakasidict

%description dict
The basic dictionary of KAKASI.

%description dict -l ja
KAKASIの基本辞書です。

%prep
%setup

%build
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

gzip --best $RPM_BUILD_DIR/%{name}-%{version}/doc/kakasi.1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -m 644 $RPM_BUILD_DIR/%{name}-%{version}/doc/kakasi.1.gz \
	$RPM_BUILD_ROOT%{_mandir}/ja/man1
%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/%{name}-config
%endif
%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING NEWS README README-ja
%{_bindir}/kakasi
%{_bindir}/mkkanwa
%{_bindir}/atoc_conv
%{_bindir}/rdic_conv
%{_bindir}/wx2_conv
%{_libdir}/libkakasi.so.*
%{_mandir}/ja/man1/kakasi.*
%{_datadir}/kakasi/itaijidict

%files devel
%defattr(-, root, root)
%{_bindir}/kakasi-config
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/%{name}-config
%endif
%{_libdir}/libkakasi.so
%{_libdir}/libkakasi.a
%{_libdir}/libkakasi.la
%{_includedir}/libkakasi.h

%files dict
%defattr(-, root, root)
%{_datadir}/kakasi/kanwadict



