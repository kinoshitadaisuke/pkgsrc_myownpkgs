# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-python-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for Python
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# pkgsrc_myownpkgs
DEPENDS+=	${PYPKGPREFIX}-edge_tts>=0:../../pkgsrc_myownpkgs/py-edge_tts
DEPENDS+=	${PYPKGPREFIX}-exifread>=0:../../pkgsrc_myownpkgs/py-exifread
DEPENDS+=	${PYPKGPREFIX}-geodatasets>=0:../../pkgsrc_myownpkgs/py-geodatasets
DEPENDS+=	${PYPKGPREFIX}-geopandas>=0:../../pkgsrc_myownpkgs/py-geopandas
DEPENDS+=	${PYPKGPREFIX}-gtts>=0:../../pkgsrc_myownpkgs/py-gtts
DEPENDS+=	${PYPKGPREFIX}-hatch>=0:../../pkgsrc_myownpkgs/py-hatch
DEPENDS+=	${PYPKGPREFIX}-instagrapi>=0:../../pkgsrc_myownpkgs/py-instagrapi
DEPENDS+=	${PYPKGPREFIX}-plotly>=0:../../pkgsrc_myownpkgs/py-plotly

# devel
DEPENDS+=	${PYPKGPREFIX}-gitpython>=0:../../devel/py-gitpython
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-ipython>=0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-pip>=0:../../devel/py-pip
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

# graphics
#DEPENDS+=	${PYPKGPREFIX}-exifread>=0:../../graphics/py-exifread
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-qrcode>=0:../../graphics/py-qrcode

# security
DEPENDS+=	${PYPKGPREFIX}-OpenSSL>=0:../../security/py-OpenSSL

# textproc
DEPENDS+=	${PYPKGPREFIX}-pdf>=0:../../textproc/py-pdf

# www
DEPENDS+=	geckodriver>=0:../../www/geckodriver
DEPENDS+=	${PYPKGPREFIX}-notebook>=0:../../www/py-notebook
DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=0:../../www/py-jupyterlab
DEPENDS+=	${PYPKGPREFIX}-selenium>=0:../../www/py-selenium

# x11
DEPENDS+=	${PYPKGPREFIX}-Tk>=0:../../x11/py-Tk

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
