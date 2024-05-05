# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-basictools-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs shells graphics math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for basic tools
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# security
DEPENDS+=	mozilla-rootcerts-openssl>=0:../../security/mozilla-rootcerts-openssl
DEPENDS+=	openssh>=0:../../security/openssh
DEPENDS+=	openssl>=0:../../security/openssl

# shells
DEPENDS+=	tcsh>=0:../../shells/tcsh
DEPENDS+=	zsh>=0:../../shells/zsh

# archivers
DEPENDS+=	bzip2>=0:../../archivers/bzip2
DEPENDS+=	bzip3>=0:../../archivers/bzip3
DEPENDS+=	gtar>=0:../../archivers/gtar
DEPENDS+=	unzip>=0:../../archivers/unzip
DEPENDS+=	xz>=0:../../archivers/xz
DEPENDS+=	zip>=0:../../archivers/zip

# benchmarks
DEPENDS+=	dhrystone>=0:../../benchmarks/dhrystone
DEPENDS+=	fib>=0:../../benchmarks/fib
DEPENDS+=	flops>=0:../../benchmarks/flops
DEPENDS+=	heapsort>=0:../../benchmarks/heapsort
DEPENDS+=	ubench>=0:../../benchmarks/ubench
DEPENDS+=	whetstone>=0:../../benchmarks/whetstone
DEPENDS+=	xengine>=0:../../benchmarks/xengine

# converters
DEPENDS+=	base64>=0:../../converters/base64
DEPENDS+=	dos2unix>=0:../../converters/dos2unix
DEPENDS+=	nkf>=0:../../converters/nkf
DEPENDS+=	skf>=0:../../converters/skf
#DEPENDS+=	unix2dos>=0:../../converters/unix2dos

# devel
DEPENDS+=	php-mode>=0:../../devel/php-mode

# editors
DEPENDS+=	emacs29>=0:../../editors/emacs29

# fonts
DEPENDS+=	arphic-ttf>=0:../../fonts/arphic-ttf
DEPENDS+=	cyberbit-ttf>=0:../../fonts/cyberbit-ttf
DEPENDS+=	intlfonts>=0:../../fonts/intlfonts
DEPENDS+=	ipaexfont>=0:../../fonts/ipaexfont
DEPENDS+=	ipafont>=0:../../fonts/ipafont
DEPENDS+=	ja-dotgothic16-ttf>=0:../../fonts/ja-dotgothic16-ttf
DEPENDS+=	ja-elisat>=0:../../fonts/ja-elisat
DEPENDS+=	ja-elisau>=0:../../fonts/ja-elisau
DEPENDS+=	ja-kaname>=0:../../fonts/ja-kaname
DEPENDS+=	ja-kappa20>=0:../../fonts/ja-kappa20
DEPENDS+=	ja-klee-ttf>=0:../../fonts/ja-klee-ttf
DEPENDS+=	ja-naga10>=0:../../fonts/ja-naga10
DEPENDS+=	ja-rampart-ttf>=0:../../fonts/ja-rampart-ttf
DEPENDS+=	ja-reggae-ttf>=0:../../fonts/ja-reggae-ttf
DEPENDS+=	ja-rocknroll-ttf>=0:../../fonts/ja-rocknroll-ttf
DEPENDS+=	ja-sazanami-ttf>=0:../../fonts/ja-sazanami-ttf
DEPENDS+=	ja-shinonome>=0:../../fonts/ja-shinonome
DEPENDS+=	ja-stick-ttf>=0:../../fonts/ja-stick-ttf
DEPENDS+=	ja-train-ttf>=0:../../fonts/ja-train-ttf
DEPENDS+=	jisx0208fonts>=0:../../fonts/jisx0208fonts
DEPENDS+=	jisx0212fonts>=0:../../fonts/jisx0212fonts
DEPENDS+=	jisx0213fonts>=0:../../fonts/jisx0213fonts
DEPENDS+=	freefont-ttf>=0:../../fonts/freefont-ttf
DEPENDS+=	kiloji-ttf>=0:../../fonts/kiloji-ttf
DEPENDS+=	kochi-ttf>=0:../../fonts/kochi-ttf
DEPENDS+=	konatu-ttf>=0:../../fonts/konatu-ttf
DEPENDS+=	koruri-ttf>=0:../../fonts/koruri-ttf
DEPENDS+=	motoya-fonts>=0:../../fonts/motoya-fonts
DEPENDS+=	mozilla-fonts>=0:../../fonts/mozilla-fonts
#DEPENDS+=	noto-cjk-fonts>=0:../../fonts/noto-cjk-fonts
#DEPENDS+=	noto-fonts>=0:../../fonts/noto-fonts
DEPENDS+=	noto-ttf>=0:../../fonts/noto-ttf
DEPENDS+=	ohruri-ttf>=0:../../fonts/ohruri-ttf
DEPENDS+=	ricty-ttf>=0:../../fonts/ricty-ttf
DEPENDS+=	takao-ex-fonts-ttf>=0:../../fonts/takao-ex-fonts-ttf
DEPENDS+=	takao-fonts-ttf>=0:../../fonts/takao-fonts-ttf
DEPENDS+=	umefont-ttf>=0:../../fonts/umefont-ttf
DEPENDS+=	vlgothic-ttf>=0:../../fonts/vlgothic-ttf
DEPENDS+=	watanabe-vfont>=0:../../fonts/watanabe_vfont

# graphics
DEPENDS+=	ImageMagick>=0:../../graphics/ImageMagick
DEPENDS+=	breeze-icons>=0:../../graphics/breeze-icons
DEPENDS+=	dcraw>=0:../../graphics/dcraw
DEPENDS+=	exif>=0:../../graphics/exif
DEPENDS+=	feh>=0:../../graphics/feh
DEPENDS+=	gimp>=0:../../graphics/gimp
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot
DEPENDS+=	inkscape>=0:../../graphics/inkscape
DEPENDS+=	jhead>=0:../../graphics/jhead
DEPENDS+=	netpbm>=0:../../graphics/netpbm
DEPENDS+=	oxygen-icons>=0:../../graphics/oxygen-icons
DEPENDS+=	ps2eps>=0:../../graphics/ps2eps
DEPENDS+=	skencil>=0:../../graphics/skencil
DEPENDS+=	tgif>=0:../../graphics/tgif
DEPENDS+=	wm-icons>=0:../../graphics/wm-icons
DEPENDS+=	xfig>=0:../../graphics/xfig
DEPENDS+=	xpaint>=0:../../graphics/xpaint
DEPENDS+=	xv>=0:../../graphics/xv

# lang
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python312>=0:../../lang/python312
DEPENDS+=	tcl>=0:../../lang/tcl

# meta-pkgs
DEPENDS+=	pkg_developer>=0:../../meta-pkgs/pkg_developer

# multimedia
DEPENDS+=	ffmpeg6>=0:../../multimedia/ffmpeg6
DEPENDS+=	mpv>=0:../../multimedia/mpv

# net
DEPENDS+=	openvpn>=0:../../net/openvpn
DEPENDS+=	rsync>=0:../../net/rsync
DEPENDS+=	wget>=0:../../net/wget
DEPENDS+=	wget2>=0:../../net/wget2
DEPENDS+=	yt-dlp>=0:../../net/yt-dlp

# print
DEPENDS+=	gv>=0:../../print/gv
DEPENDS+=	okular>=0:../../print/okular
DEPENDS+=	qpdf>=0:../../print/qpdf
DEPENDS+=	xpdf>=0:../../print/xpdf4

# textproc
DEPENDS+=	aspell>=0:../../textproc/aspell
DEPENDS+=	aspell-en>=0:../../textproc/aspell-en
DEPENDS+=	chasen>=0:../../textproc/chasen
DEPENDS+=	mecab>=0:../../textproc/mecab
DEPENDS+=	namazu>=0:../../textproc/namazu

# time
DEPENDS+=	emiclock>=0:../../time/emiclock
DEPENDS+=	oclock>=0:../../time/oclock
DEPENDS+=	xclock>=0:../../time/xclock

# wm
DEPENDS+=	fvwm3>=0:../../wm/fvwm3

# www
DEPENDS+=	curl>=0:../../www/curl

# x11
DEPENDS+=	kterm>=0:../../x11/kterm
DEPENDS+=	xterm>=0:../../x11/xterm

# pkgsrc_myownpkgs
DEPENDS+=	bizter-ttf>=0:../../pkgsrc_myownpkgs/bizter-ttf
DEPENDS+=	cica-ttf>=0:../../pkgsrc_myownpkgs/cica-ttf
DEPENDS+=	firge-ttf>=0:../../pkgsrc_myownpkgs/firge-ttf
DEPENDS+=	hackgen-ttf>=0:../../pkgsrc_myownpkgs/hackgen-ttf
DEPENDS+=	juisee-ttf>=0:../../pkgsrc_myownpkgs/juisee-ttf
DEPENDS+=	plemoljp-ttf>=0:../../pkgsrc_myownpkgs/plemoljp-ttf
DEPENDS+=	udev-gothic-ttf>=0:../../pkgsrc_myownpkgs/udev-gothic-ttf
DEPENDS+=	yatex>=0:../../pkgsrc_myownpkgs/yatex-mode

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
