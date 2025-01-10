# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-science-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs math science python
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for natural sciences
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# graphics
DEPENDS+=	gnuplot>=0:../../graphics/gnuplot

# math
DEPENDS+=	basic-stats>=0:../../math/basic-stats
DEPENDS+=	octave>=0:../../math/octave
DEPENDS+=	${PYPKGPREFIX}-lmfit>=0:../../math/py-lmfit
DEPENDS+=	${PYPKGPREFIX}-mpmath>=0:../../math/py-mpmath
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-image>=0:../../math/py-scikit-image
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-sympy>=0:../../math/py-sympy
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=0:../../math/py-uncertainties
DEPENDS+=	qcalc>=0:../../math/qcalc

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
