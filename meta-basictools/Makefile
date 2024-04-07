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
DEPENDS+=	jisx0208fonts>=0:../../fonts/jisx0208fonts
DEPENDS+=	jisx0212fonts>=0:../../fonts/jisx0212fonts
DEPENDS+=	jisx0213fonts>=0:../../fonts/jisx0213fonts
#DEPENDS+=	noto-cjk-fonts>=0:../../fonts/noto-cjk-fonts
#DEPENDS+=	noto-fonts>=0:../../fonts/noto-fonts
DEPENDS+=	noto-ttf>=0:../../fonts/noto-ttf
DEPENDS+=	ricty-ttf>=0:../../fonts/ricty-ttf

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

# input method
DEPENDS+=	mozc-elisp>=0:../../inputmethod/mozc-elisp
DEPENDS+=	mozc-server>=0:../../inputmethod/mozc-server
DEPENDS+=	mozc-tool>=0:../../inputmethod/mozc-tool

# lang
DEPENDS+=	perl>=0:../../lang/perl5
DEPENDS+=	python312>=0:../../lang/python312

# multimedia
DEPENDS+=	ffmpeg6>=0:../../multimedia/ffmpeg6
DEPENDS+=	mpv>=0:../../multimedia/mpv

# net
DEPENDS+=	openvpn>=0:../../net/openvpn
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
